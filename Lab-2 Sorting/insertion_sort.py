# Author: Bishal Sarang
# Insertion Sort Implementation

# Worst Case: O(N^2)
# Average Case: O(N^2)
# Best Case: O(N)

def insertion_sort(A):
    """
    Args:
        A (list[int]): List of integers

    Returns:
        A(list[int]): List of sorted integers
    """

    for i in range(1, len(A)):

        # set key element starting from index 1
        key = A[i]

        # Start Comparing from index i - 1 upto 0
        start = i - 1

        # Swap
        while start >= 0 and A[start] > key:
            A[start + 1] = A[start]
            start -= 1
        # Put key in its actual place
        A[start + 1] = key
        
    return A


