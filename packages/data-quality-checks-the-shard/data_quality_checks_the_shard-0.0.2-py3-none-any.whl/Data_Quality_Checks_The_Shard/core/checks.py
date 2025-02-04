import pandas as pd

class DuplicateCheck:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe
    
    def check(self):
        """Return duplicate rows."""
        return self.df[self.df.duplicated()]

class FiveNumberSummary:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe
    
    def compute(self):
        """Return statistical summary."""
        return self.df.describe()
