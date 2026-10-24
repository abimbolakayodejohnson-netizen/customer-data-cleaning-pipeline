import unittest
import pandas as pd
from customer_cleaning import clean_customer_data
class TestCleanCustomerData(unittest.TestCase):
    def test_standardizes_name_and_city(self):
        data = {
            "name": ["  AMINA Yusuf "],
            "city": [" ibadan "],
            "age": ["25"],
            "email": ["amina@example.com"]
        }

        df = pd.DataFrame(data)
        result = clean_customer_data(df)

        self.assertEqual(result["name"].iloc[0], "Amina Yusuf")
        self.assertEqual(result["city"].iloc[0], "Ibadan")
        if __name__ == "__main__":
            unittest.main()
    def test_original_data_is_unchanged(self):
        def test_original_dataframe_is_unchanged(self):
            data = {
                "name": ["  AMINA Yusuf "],
                "city": [" ibadan "],
                "age": ["25"],
                "email": ["amina@example.com"]
            }

            df = pd.DataFrame(data)
            original_df = df.copy()
            result = clean_customer_data(df)
            self.assertTrue(df.equals(original_df))

    def test_converts_age_to_number(self):
        data = {
            "name": ["Amina Yusuf"],
            "city": ["Ibadan"],
            "age": ["25"],
            "email": ["amina@example.com"]
        }

        df = pd.DataFrame(data)
        result = clean_customer_data(df)

        self.assertEqual(result["age"].iloc[0], 25)

    def test_invalid_age_becomes_nan(self):
        data = {
            "name": ["Amina Yusuf"],
            "city": ["Ibadan"],
            "age": ["twenty"],
            "email": ["amina@example.com"]
        }

        df = pd.DataFrame(data)
        result = clean_customer_data(df)

        self.assertTrue(pd.isna(result["age"].iloc[0]))