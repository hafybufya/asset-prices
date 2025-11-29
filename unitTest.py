import unittest
from  mainCode import *
import os
import tempfile

# Define the unit tests
class my_unit_tests(unittest.TestCase):



    # Tests if the csv file has been saved
    def test_csv_file_exists(self):
        """Tests if csv exists"""
        self.assertTrue(os.path.isfile('historicalData.csv'))

    #Tests if min and max value given by function is correct
    def test_min_max_index(self):
            # Creates df
            test_df = pd.DataFrame({
                "date": ["2025-01-01", "2026-05-10", "2024-03-15"],
                "value": [10, 20, 15]
            })
            # Creates temporary csv
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".csv") as temp:
                test_df.to_csv(temp.name)
                # temp.name gives you the path of the temp csv
                temp_csv = temp.name
                
            # Calling function and passing parameters
            min_val, max_val = min_max_index(temp_csv, "date")

            # Testing
            self.assertEqual(min_val, "2024-03-15")
            self.assertEqual(max_val, "2026-05-10")

            # Deletes temp_csv
            os.remove(temp_csv)


    # run the tests
if __name__ == "__main__":
    unittest.main()



