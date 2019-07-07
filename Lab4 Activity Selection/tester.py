# Author: BIshal Sarang
# Unittest for activity selectory greedy algo

import unittest
from activity_selector import select_activity_i
from activity_selector import select_activity_r

class ActivitySelectorTest(unittest.TestCase):
	
    def test_activity_selector_recursive(self):
        """
            Test recursive version of activity selector
        """
        s, e = [10, 21, 12], [20, 25, 30]
        self.assertListEqual(select_activity_r(s, e, 0), [0, 1])

        s, e = [10, 20, 25], [20, 25, 30]
        self.assertListEqual(select_activity_r(s, e, 0), [0, 1, 2])

        s, e = [10, 19, 19], [20, 25, 30]
        self.assertListEqual(select_activity_r(s, e, 0), [0])
        
    
    def test_activity_selector_iterative(self):
         """
            Test iterative version of activity selector
        """
        s, e = [10, 21, 12], [20, 25, 30]
        self.assertListEqual(select_activity_i(s, e), [0, 1])

        s, e = [10, 20, 25], [20, 25, 30]
        self.assertListEqual(select_activity_i(s, e), [0, 1, 2])
        
        s, e = [10, 19, 19], [20, 25, 30]
        self.assertListEqual(select_activity(s, e), [0])
        

if __name__ == "__main__":
	unittest.main()
