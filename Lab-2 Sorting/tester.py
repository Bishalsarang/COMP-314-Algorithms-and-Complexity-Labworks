# Author: Bishal Sarang
import random
import unittest
from insertion_sort import insertion_sort
from merge_sort import merge_sort

class SearchTestcase(unittest.TestCase):
    """
        Unit test insertion sort and merge sort
    """
    def test_insertion_sort(self):
        """
        Unit test for insertion_sort  
        """
        A = random.sample(range(100), 15)
        
        # Assert tests for element that are in the list
        self.assertListEqual(sorted(A), insertion_sort(A))


    def test_merge_sort(self):
        """
        Unit test for insertion_sort  
        """
        A = random.sample(range(100), 15)
        
        # Assert tests for element that are in the list
        self.assertListEqual(sorted(A), merge_sort(A))



if __name__ == "__main__":
    unittest.main()
    

