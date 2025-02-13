from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional, Dict, Any, Union, List
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


class SQLBaseConnector(ABC):
    """
    Abstract base class for SQL database connections and schema inspection.

    Provides interface for:
    - Database connection with multiple configuration sources
    - Schema inspection and export
    - Engine-specific connection handling
    """

    @abstractmethod
    def __init__(
        self,
        host: Optional[str] = None,
        port: Optional[int] = None,
        database: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        config_path: Optional[Path] = None,
    ):
        """Initialize database connection."""
        pass

    @abstractmethod
    def _create_engine(self, params: Dict[str, Any]):
        """Create database engine with given parameters."""
        pass

    @abstractmethod
    def _load_config(self, config_path: Optional[Path]) -> Dict[str, Any]:
        """Load configuration from file."""
        pass

    @abstractmethod
    def _get_env_vars(self) -> Dict[str, Any]:
        """Get environment variables for connection."""
        pass

    @abstractmethod
    def _resolve_params(
        self,
        host: Optional[str],
        port: Optional[int],
        database: Optional[str],
        username: Optional[str],
        password: Optional[str],
        config_path: Optional[Path],
        **kwargs,
    ) -> Dict[str, Any]:
        """Resolve connection parameters from all sources."""
        pass

    @abstractmethod
    def get_schema(
        self, schemas: Optional[Union[str, List[str]]] = None
    ) -> pd.DataFrame:
        """Get database schema information."""
        pass

    def export_schema_csv(self, path: str) -> None:
        """Export schema to CSV file."""
        df = self.get_schema()
        df.to_csv(path, index=False)
