import unittest
from  mainCode import *

import os
from pathlib import Path

# define the unit tests
class my_unit_tests(unittest.TestCase):

        # tests if the csv file has been saved
    def test_csv_file_exists(self):
        self.assertTrue(os.path.isfile('historicalData.csv'))

#DATA CHECKING

    # run the tests
if __name__ == "__main__":
    unittest.main()