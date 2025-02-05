import pandas as pd
from .checks import DuplicateCheck, FiveNumberSummary
from .schemas import DataSchema

class DataValidator:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe
    
    def run_checks(self):
        """Run all data validation checks and return results."""
        results = {
            "duplicates": DuplicateCheck(self.df).check(),
            "summary": FiveNumberSummary(self.df).compute(),
            "schema_validation": DataSchema.validate(self.df)
        }
        return results
