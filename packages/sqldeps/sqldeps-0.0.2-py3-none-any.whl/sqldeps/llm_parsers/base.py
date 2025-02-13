from abc import ABC, abstractmethod
from sqldeps.models import SQLDependency
from sqldeps.utils import merge_dependencies, merge_schemas
from sqldeps.database import PostgreSQLConnector
import json
import yaml
import sqlparse
from tqdm import tqdm
from pathlib import Path
from typing import Optional, Union, List
from loguru import logger
import importlib.resources as pkg_resources
import pandas as pd

class BaseSQLExtractor(ABC):
    """Mandatory interface for all parsers"""
    
    @abstractmethod
    def __init__(self, model: str, params: Optional[dict] = None, prompt_path: Optional[Path] = None):
        """Initialize with model name and vendor-specific params"""
        self.model = model
        self.params = params or {}
        self.prompts = self._load_prompts(prompt_path)
    
    def extract_from_query(self, sql: str) -> SQLDependency:
        """Core extraction method"""
        formatted_sql = sqlparse.format(sql, reindent=True, keyword_case="upper")
        prompt = self._generate_prompt(formatted_sql)
        response = self._query_llm(prompt)
        self.last_response = response
        return self._process_response(response)
    
    def extract_from_file(self, file_path: Union[str, Path]) -> SQLDependency:
        """Extract dependencies from a SQL file"""
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"SQL file not found: {file_path}")
            
        if file_path.suffix.lower() != '.sql':
            raise ValueError(f"File must have .sql extension: {file_path}")
            
        with open(file_path, 'r') as f:
            sql = f.read()
            
        return self.extract_from_query(sql)

    def extract_from_folder(self, folder_path: Union[str, Path], recursive: bool = False) -> SQLDependency:
        """Extract and merge dependencies from all SQL files in a folder"""
        folder_path = Path(folder_path)
        if not folder_path.exists():
            raise FileNotFoundError(f"Folder not found: {folder_path}")
            
        if not folder_path.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {folder_path}")
        
        # Define glob pattern based on recursive flag
        pattern = '**/*.sql' if recursive else '*.sql'
        
        # Get all SQL files
        sql_files = list(folder_path.glob(pattern))
        if not sql_files:
            raise ValueError(f"No SQL files found in: {folder_path}")
            
        # Extract dependencies from each file
        dependencies = []
        for sql_file in tqdm(sql_files):
            try:
                dep = self.extract_from_file(sql_file)
                dependencies.append(dep)
            except Exception as e:
                logger.warning(f"Failed to process {sql_file}: {e}")
                continue
        
        # Merge all dependencies
        return merge_dependencies(dependencies)

    def match_database_schema(
        self,
        dependencies: SQLDependency,
        db_config_path: Optional[Path] = None,
        target_schemas: Optional[List[str]] = None
    ) -> pd.DataFrame:
        """Match extracted dependencies against actual database schema"""
        # Connect to database
        conn = PostgreSQLConnector(config_path=db_config_path)
        # Get schema
        target_schemas = target_schemas or ['public']
        db_schema = conn.get_schema(schemas=target_schemas)
        
        # Convert dependencies to DataFrame
        extracted_schema = dependencies.to_dataframe()

        # Match schemas
        return merge_schemas(extracted_schema, db_schema)

    def _load_prompts(self, path: Path = None) -> dict:
        """Load prompts from a YAML file."""
        if path is None:
            with pkg_resources.files("sqldeps.configs.prompts").joinpath("default.yml").open("r") as f:
                prompts = yaml.safe_load(f)
        else:
            with open(path) as f:
                prompts = yaml.safe_load(f)
            
        required_keys = {"user_prompt", "system_prompt"}
        if not all(key in prompts for key in required_keys):
            raise ValueError(f"Prompt file must contain all required keys: {required_keys}")
        
        return prompts

    def _generate_prompt(self, sql: str) -> str:
        """
        Generate the prompt for the LLM.
        """
        return self.prompts["user_prompt"].format(sql=sql)
    
    @abstractmethod
    def _query_llm(self, prompt: str) -> str:
        """
        Query the LLM with the generated prompt to generate a response.
        """

    def _process_response(self, response: str) -> SQLDependency:
        """
        Process the LLM response into a SQLDependency object.
        """
        try:
            # Convert result into a dictionary
            result = json.loads(response)

            if "tables" not in result or "columns" not in result:
                raise ValueError(
                    "Missing required keys ('tables', 'columns') in the response."
                )

            # Convert dictory to SQLDependency
            return SQLDependency(tables=result["tables"], columns=result["columns"])

        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to decode JSON: {e}\nResponse: {response}")
