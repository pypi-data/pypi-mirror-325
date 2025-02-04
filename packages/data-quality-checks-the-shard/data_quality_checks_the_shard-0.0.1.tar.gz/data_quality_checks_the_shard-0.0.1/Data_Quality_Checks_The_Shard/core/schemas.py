import pandera as pa
import pandas as pd
from pandera import Column, DataFrameSchema, Check
from datetime import datetime

class DataSchema:
    """Define an extended dynamic Pandera schema with various checks."""
    
    # Mapping user-friendly strings to Pandera checks
    check_mapping = {
        "greater_than": lambda x: Check.greater_than(x),
        "less_than": lambda x: Check.less_than(x),
        "equal_to": lambda x: Check.equal_to(x),
        "greater_than_or_equal_to": lambda x: Check.greater_than_or_equal_to(x),
        "less_than_or_equal_to": lambda x: Check.less_than_or_equal_to(x),
        "isin": lambda x: Check.isin(x),
        "dates": lambda: Check(lambda date: isinstance(date, datetime) or date is pd.NaT, element_wise=True),
        "not_null": lambda: Check.notna(), 
        "contains": lambda x: Check.str_contains(x),
        "matches": lambda x: Check.str_match(x),
        "min_length": lambda x: Check.str_length(min_value=int(x)),  # using Pandera's str_length check
        "max_length": lambda x: Check.len(x).value <= int(x),
        "before_date": lambda x: Check(lambda date: isinstance(date, datetime) and date < x, element_wise=True),
        "after_date": lambda x: Check(lambda date: isinstance(date, datetime) and date > x, element_wise=True),
        "before_or_on_date": lambda x: Check(lambda date: isinstance(date, datetime) and date <= x, element_wise=True),
        "after_or_on_date": lambda x: Check(lambda date: isinstance(date, datetime) and date >= x, element_wise=True),
        "between_dates": lambda x, y: Check(lambda date: isinstance(date, datetime) and x <= date <= y, element_wise=True),
    }

    
    def __init__(self, column_info: list):
        """
        Initialize the schema with user-provided column info in a simplified format.
        
        :param column_info: List of tuples with column details.
                            Each tuple contains: (column_name, dtype, check_type, check_value, nullable)
                            Example:
                            [
                                ("column1", float, "greater_than", 0, False),
                                ("column2", str, "isin", ["A", "B", "C"], False),
                                ("column3", datetime, "dates", None, True)
                            ]
        """
        self.column_info = column_info
        self.schema = self.create_schema()

    def create_schema(self):
        """Create the schema dynamically based on the simplified column info."""
        schema_dict = {}
        
        for column_name, dtype, check_type, check_value, nullable in self.column_info:
            # Get the check function from the mapping based on the user's input
            check_function = self.check_mapping.get(check_type)
            
            if check_function:
                # Apply the check function and pass the check_value if necessary
                if isinstance(check_value, tuple) and len(check_value) == 2:
                    check = check_function(*check_value)  # for between_dates
                else:
                    check = check_function(check_value) if check_value is not None else check_function()
                schema_dict[column_name] = Column(dtype, check, nullable=nullable)
            else:
                raise ValueError(f"Unknown check type: {check_type}")
        
        return DataFrameSchema(schema_dict)

    def validate(self, df):
        """Validate the dataframe against the dynamically created schema."""
        try:
            return self.schema.validate(df)
        except pa.errors.SchemaError as e:
            return str(e)

# Example of defining a schema with date comparison checks
column_info = [
    ("column1", float, "greater_than", 0, False),
    ("column2", str, "isin", ["A", "B", "C"], False),
    ("column3", datetime, "dates", None, True),
    ("column4", datetime, "before_date", datetime(2025, 1, 1), False),  # Example: before 2025-01-01
    ("column5", datetime, "after_date", datetime(2020, 1, 1), False),   # Example: after 2020-01-01
    ("column6", datetime, "between_dates", (datetime(2025, 1, 5), datetime(2025, 1, 10)), False)  # Example: between 2025-01-05 and 2025-01-10
]

# Initialize schema
schema = DataSchema(column_info)

# Example DataFrame for validation
df = pd.DataFrame({
    "column1": [1.5, 3.0],
    "column2": ["A", "C"],
    "column3": [datetime.now(), pd.NaT],
    "column4": [datetime(2024, 12, 31), datetime(2024, 5, 5)],  # column4 should be before 2025-01-01
    "column5": [datetime(2022, 6, 15), datetime(2022, 3, 10)],  # column5 should be after 2020-01-01
    "column6": [datetime(2024, 1, 8), datetime(2025, 1, 9)]  # column6 should be between 2025-01-05 and 2025-01-10
})

# Validate the DataFrame
validation_result = schema.validate(df)
print(validation_result)
