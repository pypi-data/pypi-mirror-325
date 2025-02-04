import unittest
import pandas as pd
from datetime import datetime
from ..core.schemas import DataSchema  # Replace 'your_module' with the actual module name

class TestDataSchema(unittest.TestCase):
    def setUp(self):
        # Define the schema for testing
        self.column_info = [
            ("column1", float, "greater_than", 0, False),
            ("column2", str, "isin", ["A", "B", "C"], False),
            ("column3", datetime, "dates", None, True),
            ("column4", datetime, "before_date", datetime(2025, 1, 1), False),
            ("column5", datetime, "after_date", datetime(2020, 1, 1), False),
            ("column6", datetime, "between_dates", (datetime(2025, 1, 5), datetime(2025, 1, 10)), False)
        ]
        self.schema = DataSchema(self.column_info)

    def test_valid_dataframe(self):
        # Create a valid DataFrame
        valid_df = pd.DataFrame({
            "column1": [1.5, 3.0],
            "column2": ["A", "C"],
            "column3": [datetime.now(), pd.NaT],
            "column4": [datetime(2024, 12, 31), datetime(2024, 5, 5)],
            "column5": [datetime(2022, 6, 15), datetime(2022, 3, 10)],
            "column6": [datetime(2025, 1, 8), datetime(2025, 1, 9)]
        })

        # Validate the DataFrame
        result = self.schema.validate(valid_df)
        self.assertIsInstance(result, pd.DataFrame)  # Validation should return a DataFrame

    def test_invalid_dataframe(self):
        # Create an invalid DataFrame
        invalid_df = pd.DataFrame({
            "column1": [-1.0, 3.0],  # Invalid: column1 should be greater than 0
            "column2": ["D", "C"],   # Invalid: column2 should be in ["A", "B", "C"]
            "column3": [datetime.now(), pd.NaT],
            "column4": [datetime(2025, 1, 2), datetime(2024, 5, 5)],  # Invalid: column4 should be before 2025-01-01
            "column5": [datetime(2019, 6, 15), datetime(2022, 3, 10)],  # Invalid: column5 should be after 2020-01-01
            "column6": [datetime(2025, 1, 4), datetime(2025, 1, 9)]  # Invalid: column6 should be between 2025-01-05 and 2025-01-10
        })

        # Validate the DataFrame
        result = self.schema.validate(invalid_df)
        self.assertIsInstance(result, str)  # Validation should return an error message

    def test_missing_column(self):
        # Create a DataFrame with a missing column
        missing_column_df = pd.DataFrame({
            "column1": [1.5, 3.0],
            "column2": ["A", "C"],
            "column3": [datetime.now(), pd.NaT],
            "column4": [datetime(2024, 12, 31), datetime(2024, 5, 5)],
            "column5": [datetime(2022, 6, 15), datetime(2022, 3, 10)]
            # Missing column6
        })

        # Validate the DataFrame
        result = self.schema.validate(missing_column_df)
        self.assertIsInstance(result, str)  # Validation should return an error message

    def test_nullable_column(self):
        # Create a DataFrame with a nullable column
        nullable_df = pd.DataFrame({
            "column1": [1.5, 3.0],
            "column2": ["A", "C"],
            "column3": [datetime.now(), pd.NaT],  # column3 is nullable
            "column4": [datetime(2024, 12, 31), datetime(2024, 5, 5)],
            "column5": [datetime(2022, 6, 15), datetime(2022, 3, 10)],
            "column6": [datetime(2025, 1, 8), datetime(2025, 1, 9)]
        })

        # Validate the DataFrame
        result = self.schema.validate(nullable_df)
        self.assertIsInstance(result, pd.DataFrame)  # Validation should return a DataFrame

if __name__ == "__main__":
    unittest.main()