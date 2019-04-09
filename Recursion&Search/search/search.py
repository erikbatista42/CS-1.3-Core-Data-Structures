#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # base case
    if array[index] == item: 
        return index # found
    # recursive case
    elif item in array: # look up - O(n) 
        return linear_search_recursive(array, item, index + 1)
    return None # not found


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    left = 0
    right = len(array) -1

    while (left >= right): # loop through this as long as left & right are in the correct positions
        midpoint = (left + right) // 2
        if (array[midpoint] == item):
            return True
        elif (array[midpoint] < item):
            # go right
            midpoint = midpoint - 1
        else:
            # go left
            midpoint = midpoint + 1
    return None # not found


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
