def factorial_iterative(n):
    # TODO: implement the factorial function iteratively here
    pass
    # once implemented, change factorial (above) to call factorial_iterative
    # to verify that your iterative implementation passes all tests
    fibList = [0, 1, 1]
    currentIndex = len(fibList) - 1
    while (currentIndex < n):
        currentIndex = len(fibList) - 1 #1
        fibNum = fibList[currentIndex] + fibList[currentIndex - 1]
        fibList.append(fibNum)
        currentIndex += 1
    return fibList


# def binary_search_iterative(array, item):
#     # TODO: implement binary search iteratively here
#     left = 0
#     right = len(array) -1

#     while (left <= right): # loop through this as long as left & right are in the correct positions
#         midpoint = (left + right) // 2
#         if (array[midpoint] == item):
#             return True
#         elif (array[midpoint] < item):
#             # go right
#             right = midpoint - 1
#         else:
#             # go left
#             left = midpoint + 1
#     return None # not found

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
    else:
        return linear_search_recursive(array, item, index + 1)
    return None # not found

def binary_search_iterative(array, item):
    left = 0
    right = len(array) -1

    while (left <= right):
        midpoint = (left + right) // 2
        if (array[midpoint] == item):
            return True # found
        elif (array[midpoint] < item):
            # go right
            left = midpoint + 1
        elif (array[midpoint] > item):
            # go left
            right = midpoint - 1
        else:
            return None # not found

if __name__ == "__main__":
    my_array = [1,2,3,4,5,6,7]
    # bin_search = binary_search_iterative(my_array, 6)
    # print(bin_search)
    # print(linear_search_recursive(my_array, 3))
    # print(linear_search_iterative(my_array, 3))
    print(binary_search_iterative(my_array, 1))