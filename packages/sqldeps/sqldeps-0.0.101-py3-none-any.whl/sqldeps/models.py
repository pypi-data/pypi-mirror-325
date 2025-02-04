from dataclasses import dataclass
from typing import List, Dict

@dataclass  
class SQLDependency:
    """Data class to hold SQL dependency information."""
    tables: List[str]
    columns: Dict[str, List[str]]

    def __post_init__(self):
        self.tables.sort()
        self.columns = {
            table: sorted(cols) for table, cols in sorted(self.columns.items())
        }

    def to_dict(self) -> Dict:
        return {"tables": self.tables, "columns": self.columns}
