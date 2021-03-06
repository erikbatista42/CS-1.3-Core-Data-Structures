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
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

    if index > len(array) -1:
        return None # not found
    # base case - when we have found item
    if array[index] == item:
        return index
    else:
        # recurse to the next index
        return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    '''
    O(log n) time - because we're cutting half at every iteration
    O(1) space - we're not making any memory
    '''
    left = 0
    right = len(array)-1
    while left <= right:
        middle = (left + right) // 2
        
        if array[middle] == item:
            return middle
        elif array[middle] < item:
            left = middle + 1
        else:
            right = middle - 1

    return None # not found

# edge case is a tricky input

def binary_search_recursive(array, item, left=None, right=None):
    # O(log n) space + time - because we're using the stack as space and cutting half at every iteration
    if item in array:
        # set left and right starter values
        if left == None and right == None:
            return binary_search_recursive(array, item, left=0, right=((len(array) -1) // 2))
        
        # base case
        if (array[right] == item):
            return right # => found
        
        # recursive cases
        if left <= right:
            if (array[right] < item): 
                return binary_search_recursive(array, item, left = (left + right) // 2, right= right + 1)
            elif (array[right] > item): 
                return binary_search_recursive(array, item, left = (left + right) // 2, right= right -1)
    return None # not found