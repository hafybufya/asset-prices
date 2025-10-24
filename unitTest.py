import unittest
from  mainCode import *
import os
import tempfile
import datetime
# define the unit tests
class my_unit_tests(unittest.TestCase):


    def test_read_nordic_date(self):
         pass
        # tests if the csv file has been saved
    def test_csv_file_exists(self):
        """Tests if csv exists"""
        self.assertTrue(os.path.isfile('historicalData.csv'))

    def test_min_max_index(self):
            #creates df
            test_df = pd.DataFrame({
                "date": ["2025-01-01", "2026-05-10", "2024-03-15"],
                "value": [10, 20, 15]
            })
            #creates temporary csv
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".csv") as temp:
                test_df.to_csv(temp.name)
                #temp.name gives you the path of the temp csv
                temp_csv = temp.name
                
            #calling function and passing parameters
            min_val, max_val = min_max_index(temp_csv, "date")

            #testing
            self.assertEqual(min_val, "2024-03-15")
            self.assertEqual(max_val, "2026-05-10")

            # deletes temp_csv
            os.remove(temp_csv)


    # run the tests
if __name__ == "__main__":
    unittest.main()



