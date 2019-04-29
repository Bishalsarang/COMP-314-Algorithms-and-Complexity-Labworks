# Author: Bishal Sarang
# Merge Sort Implementation

# Worst Case: O(nlog(n))
# Average Case: O(nlog(n))
# Best Case: O(nlog(n))


def merge_sort(A):
    """
    Recursive Merge Sort   
    Args:
        A (list[int]): List of integers

    Returns:
        A(list[int]): List of sorted integers
    """

    # Divide and sort unless the array size is 1
    # If the array size is 1 then it is already sorted
    if len(A) > 1:
        
        mid = len(A) // 2

        # Left Half Array
        left_half = A[: mid]
        # Right Half Array
        right_half = A[mid:]

        # Recursively Sort Left Half
        merge_sort(left_half)

        # Recursively Sort Right Half
        merge_sort(right_half)


        # Merge Left Half and Right Half
        # i, j, k are the pointers to left_half, right_half and the array itself
        i , j, k = 0, 0 , 0


        # Put the element to the array from left_half and right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                A[k] = left_half[i]
                i += 1
            else:
                A[k] = right_half[j]
                j += 1
            k += 1

        # If left half is still remaining
        # Consider l = [4, 5, 6] and r = [1, 2, 3]
        # Then A = [1, 2, 3] with 3 spaces to be filled
        # Fill the remaining part of array with left_half remaining
        while i < len(left_half):
            A[k] = left_half[i]
            i += 1
            k += 1

        # If right half is still remaining
        # Consider r = [4, 5, 6] and l = [1, 2, 3]
        # Then A = [1, 2, 3] with 3 spaces to be filled
        # Fill the remaining part of array with right_half remaining   
        while j < len(right_half):
            A[k] = right_half[j]
            j += 1
            k += 1
        
    return A
