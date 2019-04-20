# Author: Bishal Sarang
# Implementation of binary search


# Best Case: O(1)
# Worst Case: O(log(N))
# Average Case: O(log(N))
def iterative_binary_search(A, l, h, target):
    """
    Iterative version of binary search    
    Args:
        A (list[int]): List of integers
        l (int): The lower index 
        h (int): The upper index
        target (int): The target to be searched
        
    Returns:
        int: The index of the target if found else -1
    """
    while l <= h:
        mid = (l + h) // 2

        # If the target element is found return the index
        if A[mid] == target:
            return mid
        # Search right half
        elif A[mid] < target:
            l = mid + 1
        # Search left half
        else:
            h = mid - 1
            
    # return -1 if not found
    return -1
    

def recursive_binary_search(A, l, h, target):
    """
    Recursive version of binary search    
    Args:
        A (list[int]): List of integers
        l (int): The lower index 
        h (int): The upper index
        target (int): The target to be searched
        
    Returns:
        int: The index of the target if found else -1
    """

    if l <= h:
        mid = (l + h) // 2

        # If element is found return the index
        if A[mid] == target:
            return mid
        # Search left half
        elif A[mid] > target:
            return recursive_binary_search(A, l, mid - 1, target)
        # Search right half
        return recursive_binary_search(A, mid + 1, h, target)
    
    return -1 
