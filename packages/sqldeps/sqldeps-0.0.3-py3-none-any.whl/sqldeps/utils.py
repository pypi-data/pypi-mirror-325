import pandas as pd
from sqldeps.models import SQLDependency
from typing import List, Dict, Set

def merge_dependencies(dependencies: List[SQLDependency]) -> SQLDependency:
    """
    Merges multiple SQLDependency objects into a single one with distinct tables and columns.

    If a table has '*' in its column list, only '*' will be kept, and other columns will be ignored.

    Args:
        dependencies (List[SQLDependency]): List of SQLDependency objects.

    Returns:
        SQLDependency: A merged dependency object with distinct tables and columns.
    """
    merged_tables: Set[str] = set()
    merged_columns: Dict[str, Set[str]] = {}

    for dep in dependencies:
        merged_tables.update(dep.tables)
        for table, columns in dep.columns.items():
            if "*" in columns:
                merged_columns[table] = {"*"}
            else:
                merged_columns.setdefault(table, set()).update(columns)

    return SQLDependency(
        tables=list(merged_tables),
        columns={table: list(columns) for table, columns in merged_columns.items()}
    )


def merge_schemas(
        df_extracted_schema: pd.DataFrame, 
        df_db_schema: pd.DataFrame
    ) -> pd.DataFrame:
    """
    Matches extracted SQL dependencies with the actual database schema, 
    handling both exact schema matches and schema-agnostic matches.
    Expands wildcards ('*') to match all columns from the relevant table(s).

    Args:
        df_extracted_schema (pd.DataFrame): Extracted table-column dependencies.
        df_db_schema (pd.DataFrame): Actual database schema information.

    Returns:
        pd.DataFrame: Merged schema with an `exact_match` flag.
    """
    # Create copy to avoid modifying input
    df_extracted = df_extracted_schema.copy()
    df_extracted['exact_match'] = pd.Series(dtype='boolean')
    
    # Expand wildcards (*) to include all relevant columns
    if (wildcard_mask := df_extracted['column'] == '*').any():
        regular_deps = df_extracted[~wildcard_mask]
        wildcard_deps = df_extracted[wildcard_mask]
        expanded_wildcard_deps = []

        for _, row in wildcard_deps.iterrows():
            mask = df_db_schema['table'] == row['table']
            if pd.notna(row['schema']):
                mask &= df_db_schema['schema'] == row['schema']
                wildcard_schema = (
                    df_db_schema[mask][['schema', 'table', 'column']]
                    .assign(exact_match=True)
                )
            else:
                wildcard_schema = (
                    df_db_schema[mask][['schema', 'table', 'column']]
                    .assign(exact_match=False)
                )
            expanded_wildcard_deps.append(wildcard_schema)
            
        df_extracted = pd.concat([regular_deps, *expanded_wildcard_deps], ignore_index=True)
    
    # Exact schema matches
    exact_matches = (
        df_extracted[df_extracted['schema'].notna()]
        .merge(df_db_schema, how="inner")
        .fillna({'exact_match': True})
    )
    
    # Schema-agnostic matches (ignoring schema column)
    schemaless_matches = (
        df_extracted[df_extracted['schema'].isna()]
        .drop(columns='schema')
        .merge(df_db_schema, how="inner")
        .fillna({'exact_match': False})
    )
    
    # Combine results & remove duplicates with priority to exact matches
    df_merged_schemas = (
        pd.concat([exact_matches, schemaless_matches], ignore_index=True)
        .reindex(columns=['schema','table','column','data_type','exact_match'])
        # Sort values to give priority to exact matches
        .sort_values(
            by=['schema','table','column','data_type','exact_match'],
            ascending=[True,True,True,True,False]
        )
        # Drop duplicates (keep exact matches)
        .drop_duplicates(subset=['schema','table','column','data_type'])
        .reset_index(drop=True)
    )
    
    return df_merged_schemas


def schema_diff(df_extracted_schema: pd.DataFrame, df_db_schema: pd.DataFrame, copy: bool=True) -> pd.DataFrame:
    """
    Checks if extracted schema entries exist in the database schema.

    Args:
        df_extracted_schema (pd.DataFrame): Extracted table-column dependencies.
        df_db_schema (pd.DataFrame): Actual database schema information.

    Returns:
        pd.DataFrame: The extracted schema with an added `exist_db` flag.
    """
    # Copy dataframe to avoid in-place update
    if copy:
        df_extracted_schema = df_extracted_schema.copy()

    # Create sets for quick lookup
    db_exact_matches = set(zip(df_db_schema["schema"], df_db_schema["table"], df_db_schema["column"]))
    db_table_matches = set(zip(df_db_schema["schema"], df_db_schema["table"]))
    db_schema_agnostic = set(zip(df_db_schema["table"], df_db_schema["column"]))
    db_table_agnostic = set(df_db_schema["table"])

    def check_existence(row):
        """Helper function to determine if a row exists in the DB schema."""
        if pd.notna(row["schema"]):
            if row["column"] == "*":
                return (row["schema"], row["table"]) in db_table_matches
            return (row["schema"], row["table"], row["column"]) in db_exact_matches
        else:
            if row["column"] == "*":
                return row["table"] in db_table_agnostic
            return (row["table"], row["column"]) in db_schema_agnostic

    # Apply vectorized check
    df_extracted_schema["match_db"] = df_extracted_schema.apply(check_existence, axis=1)

    return df_extracted_schema
