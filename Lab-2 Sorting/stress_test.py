# Author: Bishal Sarang
# Stress test with random data for searching algorithm

import random

from insertion_sort import insertion_sort
from merge_sort import merge_sort


def random_stress_test():
    """
    Function to stress test with random data
    Args:
    
    Returns:
        None
    """
    # Generate random number for number of testcases
    testcases = random.randint(1, 2000)

    # For every testcase generate a random list and search for random value
    # Throw assertion error if code fails
    for i in range(testcases):

        # Generate random size from 1 to 899
        size = random.randint(1, 900)

        # Generate a random list of size by choosing elemnt from [0..9999]
        A = random.sample(range(10000), size)

        # Sorted Array
        sorted_A = sorted(A)


        # Assert if our code is working as expected for
        # Insertion Sort and Merge Sort
        assert(insertion_sort(A) == sorted_A)
        assert(merge_sort(A) == sorted_A)
        
       

        print("Testcase {} passed".format(i + 1))
    print("Congratulations all {} testcases ran successfully".format(testcases))
        
if __name__ == "__main__":

    # Call random Stress test
    random_stress_test()
    print("All stress tests and corner tests ran successfully")
    
