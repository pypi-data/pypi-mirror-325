from sqlalchemy import create_engine, inspect
from pathlib import Path
from typing import Optional, Dict, Any, Union, List
from urllib.parse import quote_plus
import yaml
import os

from loguru import logger
import pandas as pd
from .base import SQLBaseConnector


class PostgreSQLConnector(SQLBaseConnector):
    """
    PostgreSQL database utility class that provides secure connection management and schema inspection capabilities.

    Supports multiple configuration sources for database connection parameters:
    - Direct parameters in constructor
    - YAML configuration file
    - Environment variables (.env file)
    - PostgreSQL password file (~/.pgpass)

    Configuration priority for host, port, database, and username (highest to lowest):
    1. Direct parameters in constructor
    2. YAML config file
    3. Environment variables
    4. .pgpass for password lookup
    """

    def __init__(
        self,
        host: Optional[str] = None,
        port: Optional[int] = None,
        database: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        config_path: Optional[Path] = None
    ):
        """
        Initialize database connection with provided configuration.

        Args:
            host: Database host address
            port: Database port (default: 5432)
            database: Database name
            username: Database username
            password: Database password
            config_path: Path to optional YAML config file

        Required Parameters:
            The following must be provided through one of the configuration sources:
            - host
            - database
            - username
            - password (either through .pgpass or other sources)

        Environment Variables:
            DB_HOST: Database host
            DB_PORT: Database port
            DB_NAME: Database name
            DB_USER: Database username
            DB_PASSWORD: Database password

        YAML Config Format:
            database:
                host: localhost
                port: 5432
                database: mydb
                username: user
                password: pass
        """
        # Load and validate connection parameters
        connection_params = self._resolve_params(
            host, port, database, username, password, config_path
        )

        # Create engine
        self.engine = self._create_engine(connection_params)
        self.inspector = inspect(self.engine)

    def _load_config(self, config_path: Optional[Path]) -> Dict[str, Any]:
        """Load optional YAML config file if provided."""
        if not config_path:
            return {}

        try:
            with open(config_path) as f:
                return yaml.safe_load(f)
        except Exception as e:
            logger.warning(f"Failed to load config file: {e}")
            return {}

    def _get_env_vars(self) -> Dict[str, Any]:
        """Extract environment variables with standard PostgreSQL naming."""
        return {
            "host": os.getenv("DB_HOST"),
            "port": os.getenv("DB_PORT"),
            "database": os.getenv("DB_NAME"),
            "username": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
        }

    def _get_password_from_pgpass(
        self, username: str, host: str, database: str, port: Union[str, int], password: Optional[None]
    ) -> Optional[str]:
        """
        Attempt to find matching password in .pgpass file.
        
        Args:
            username: Database username
            host: Database host
            database: Database name
            port: Database port
            password: placeholder to enable receiving all params retrieved from the other sources
            
        Returns:
            Matching password if found, None otherwise
        """
        pgpass_path = Path.home() / ".pgpass"
        
        try:
            input_creds = [str(host), str(port), database, username]
            
            with open(pgpass_path, "r") as f:
                for line in f:
                    line = line.strip()

                    # Skip comments
                    if line.startswith("#"):
                        continue
                        
                    pgpass_host, pgpass_port, pgpass_database, pgpass_username, pgpass_password = line.split(":")
                    pgpass_creds = [pgpass_host, pgpass_port, pgpass_database, pgpass_username]
                    
                    pgpass_matches = True
                    for input_item, pgpass_item in zip(input_creds, pgpass_creds):
                        if pgpass_item == "*":
                            continue
                        if pgpass_item != input_item:
                            pgpass_matches = False
                            break
                            
                    if pgpass_matches:
                        return pgpass_password

        except Exception as e:
            logger.warning(f"Failed to read .pgpass file: {e}")
            
        return None

    def _resolve_params(
        self,
        host: Optional[str],
        port: Optional[int],
        database: Optional[str],
        username: Optional[str],
        password: Optional[str],
        config_path: Optional[Path]
    ) -> Dict[str, Any]:
        """
        Resolve connection parameters using priority hierarchy.
        
        For host, port, database, and username:
        1. Direct parameters
        2. Config file
        3. Environment variables
        
        When the password is not provided through the sources above:
            - Look up in .pgpass using the provided credentials
        """
        params = {
            "host": None,
            "port": 5432,     # Default PostgreSQL port
            "database": None,
            "username": None,
            "password": None,
        }

        # Load all potential sources
        config_params = self._load_config(config_path).get("database", {})
        env_vars = self._get_env_vars()
        direct_params = {
            "host": host,
            "port": port,
            "database": database,
            "username": username,
            "password": password,
        }

        # Apply sources in priority order for all params except password
        sources = [
            env_vars,      # Lowest priority
            config_params, # Second priority
            direct_params, # Highest priority
        ]

        for source in sources:
            for key in params:
                if source.get(key) is not None:
                    params[key] = source[key]

        # Validate required non-password parameters
        if not all([params["host"], params["database"], params["username"]]):
            raise ValueError(
                "Missing required database parameters (host, database, or username). "
                "Must be provided through direct parameters, config file or environment variables."
            )

        # Fall back to .pgpass for password lookup
        if not params['password']:
            params["password"] = self._get_password_from_pgpass(**params)

            # Validate password
            if not params["password"]:
                raise ValueError(
                    "Missing password. Must be provided through direct parameters, "
                    "config file, environment variables, or available at .pgpass"
                )

        return params

    def _create_engine(self, params: Dict[str, Any]):
        """Create SQLAlchemy engine without storing credentials."""
        connection_string = (
            f"postgresql://{params['username']}:{quote_plus(params['password'])}@"
            f"{params['host']}:{params['port']}/{params['database']}"
        )

        # Clear sensitive data
        params.clear()

        return create_engine(connection_string, connect_args={"connect_timeout": 10})

    def get_schema(
        self, schemas: Optional[Union[str, List[str]]] = None
    ) -> pd.DataFrame:
        """
        Retrieve database schema information as a DataFrame.

        Args:
            schemas: Optional schema name or list of schema names to filter results.
                    If None, returns information for all schemas.

        Returns:
            DataFrame with columns: schema, table, column, data_type
        """

        if schemas is None:
            schema_list = self.inspector.get_schema_names()
        elif isinstance(schemas, str):
            schema_list = [schemas]
        elif isinstance(schemas, list):
            schema_list = schemas
        else:
            raise TypeError("schemas must be None, string, or list of strings")

        schema_data = []
        for schema in schema_list:
            for table_name in self.inspector.get_table_names(schema=schema):
                for column in self.inspector.get_columns(table_name, schema=schema):
                    schema_data.append(
                        {
                            "schema": schema,
                            "table": table_name,
                            "column": column["name"],
                            "data_type": str(column["type"]),
                        }
                    )

        return pd.DataFrame(schema_data)

    def export_schema_csv(self, path: str):
        """Export schema to CSV"""
        df = self.get_schema_df()
        df.to_csv(path, index=False)
