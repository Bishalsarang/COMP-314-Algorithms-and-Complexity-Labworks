# Author: Bishal Sarang
# Implementation of linear search

# Best Case: O(1)
# Worst Case: O(N)
# Average Case: O(N)

def linear_search(A, target):
    """
    Linear Search   
    Args:
        A (list[int]): List of integers
        elem (int): The target to be searched
        
    Returns:
        int: The index of the target if found else -1
    """
    for i, elem in enumerate(A):
        # return index if the target is found
        if A[i] == target:
            return i

    # return -1 if not found
    return -1
    

