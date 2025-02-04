from abc import ABC, abstractmethod
from sqldeps.models import SQLDependency
import json
import yaml
import sqlparse
from pathlib import Path
from typing import Optional

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

    def _load_prompts(self, path: Path = None) -> dict:
        """Load prompts from a YAML file."""
        if path is None:
            path = Path(__file__).parent.parent / "configs" / "prompts" / "default.yml"
        
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
