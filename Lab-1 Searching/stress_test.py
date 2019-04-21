# Author: Bishal Sarang
# Stress test with random data for searching algorithm

import random

from linear_search import linear_search
from binarysearch import iterative_binary_search
from binarysearch import recursive_binary_search

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
        # Sort the list for binary search
        A = sorted(random.sample(range(10000), size))

        # Choose random element from the array
        target = random.choice(A)
        # Find the actual index of the target element
        actual_index = A.index(target)

        # Assert if our code is working as expected for
        # Linear Search and Binary Search
        assert(linear_search(A,target) == actual_index )
        assert(iterative_binary_search(A, 0, size - 1, target) == actual_index )
        assert(recursive_binary_search(A, 0, size - 1, target) == actual_index )

        print("Testcase {} passed".format(i + 1))
    print("Congratulations all {} testcases ran successfully".format(testcases))
        
if __name__ == "__main__":

    # Call random Stress test
    random_stress_test()

    # Some Corner cases
    A = [1]
    size = 1
    assert(linear_search(A, 1) == 0)
    assert(iterative_binary_search(A, 0, size - 1, 1) == 0)
    assert(recursive_binary_search(A, 0, size - 1, 1) == 0)
    
    assert(linear_search(A, 99) == -1)
    assert(iterative_binary_search(A, 0, size - 1, 99) == -1)
    assert(recursive_binary_search(A, 0, size - 1, 99) == -1)

    assert(linear_search(A, 0) == -1)
    assert(iterative_binary_search(A, 0, size - 1, 0) == -1)
    assert(recursive_binary_search(A, 0, size - 1, 0) == -1)


    A = [1, 2]
    size = 2
    assert(linear_search(A, 1) == 0)
    assert(iterative_binary_search(A, 0, size - 1, 1) == 0)
    assert(recursive_binary_search(A, 0, size - 1, 1) == 0)

    assert(linear_search(A, 2) == 1)
    assert(iterative_binary_search(A, 0, size - 1, 2) == 1)
    assert(recursive_binary_search(A, 0, size - 1, 2) == 1)
    
    assert(linear_search(A, 99) == -1)
    assert(iterative_binary_search(A, 0, size - 1, 99) == -1)
    assert(recursive_binary_search(A, 0, size - 1, 99) == -1)

    assert(linear_search(A, 0) == -1)
    assert(iterative_binary_search(A, 0, size - 1, 0) == -1)
    assert(recursive_binary_search(A, 0, size - 1, 0) == -1)

    print("All stress tests and corner tests ran successfully")
    
