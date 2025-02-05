import unittest
import pandas as pd
from ..core.checks import DuplicateCheck, FiveNumberSummary  

class TestDataFrameFunctions(unittest.TestCase):
    
    def setUp(self):
        """Setup test data."""
        # Sample DataFrame with duplicate rows for testing DuplicateCheck
        self.df_with_duplicates = pd.DataFrame({
            "A": [1, 2, 2, 4, 5],
            "B": [10, 20, 20, 40, 50]
        })
        
        # Sample DataFrame for testing FiveNumberSummary
        self.df_for_summary = pd.DataFrame({
            "A": [1, 2, 3, 4, 5],
            "B": [10, 20, 30, 40, 50]
        })

    def test_duplicate_check(self):
        """Test duplicate rows detection."""
        duplicate_check = DuplicateCheck(self.df_with_duplicates)
        duplicates = duplicate_check.check()

        # Test that the duplicated rows are returned correctly
        self.assertEqual(len(duplicates), 1, "Expected 1 duplicate row.")  # Only 1 duplicate row (index 2)
        self.assertTrue(duplicates.equals(self.df_with_duplicates.iloc[2:3]), "The duplicate rows don't match.")

    def test_five_number_summary(self):
        """Test five-number summary (describe function)."""
        summary = FiveNumberSummary(self.df_for_summary)
        result = summary.compute()

        # Test that the result is a DataFrame and contains the correct statistical summary
        self.assertIsInstance(result, pd.DataFrame, "The result should be a pandas DataFrame.")
        self.assertTrue("A" in result.columns, "Summary does not contain 'A' column.")
        self.assertTrue("B" in result.columns, "Summary does not contain 'B' column.")

        # Test that the summary contains the expected count, min, max, mean, etc.
        self.assertGreater(result["A"]["count"], 0, "The 'A' column should have non-zero count.")
        self.assertGreater(result["B"]["mean"], 0, "The 'B' column should have a positive mean.")

if __name__ == '__main__':
    unittest.main()
