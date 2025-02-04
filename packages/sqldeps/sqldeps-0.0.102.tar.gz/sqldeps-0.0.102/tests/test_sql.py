import json
import pytest
from sqldeps.llm_parsers import OpenaiExtractor

@pytest.fixture()
def extractor():
    params = {"temperature": 0, "top_p": 1}  # Deterministic outputs for testing
    return OpenaiExtractor(params=params)

## TODO: Add test for invalid SQL query
# def test_invalid_sql(extractor):
#     """Test handling of invalid SQL"""
#     with pytest.raises(Exception):
#         extractor.extract_from_query("SELECT * FRO users")

@pytest.mark.parametrize("sql_file, expected_output_file", [
    ("tests/test_sql/example1.sql", "tests/test_sql_outputs/example1_expected.json"),
    ("tests/test_sql/example2.sql", "tests/test_sql_outputs/example2_expected.json"),
    ("tests/test_sql/example3.sql", "tests/test_sql_outputs/example3_expected.json"),
    ("tests/test_sql/example4.sql", "tests/test_sql_outputs/example4_expected.json"),
    ("tests/test_sql/example5.sql", "tests/test_sql_outputs/example5_expected.json"),
    ("tests/test_sql/example6.sql", "tests/test_sql_outputs/example6_expected.json"),
    ("tests/test_sql/example7.sql", "tests/test_sql_outputs/example7_expected.json"),
    ("tests/test_sql/example8.sql", "tests/test_sql_outputs/example8_expected.json"),
    ("tests/test_sql/example9.sql", "tests/test_sql_outputs/example9_expected.json"),
    ("tests/test_sql/example10.sql", "tests/test_sql_outputs/example10_expected.json"),
])
def test_sql_dependency_extraction(sql_file, expected_output_file, extractor):
    print(sql_file, expected_output_file)
    # Load SQL code
    with open(sql_file, "r") as f:
        sql = f.read()

    # Load expected output
    with open(expected_output_file, "r") as f:
        expected_output = json.load(f)

    # Run the extractor
    dependency = extractor.extract_from_query(sql)

    # Assert the output matches the expected
    assert dependency.to_dict() == expected_output
