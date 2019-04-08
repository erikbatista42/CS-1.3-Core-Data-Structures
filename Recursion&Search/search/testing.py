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
#     sorted_array = sorted(array)
#     found = False


#     if (sorted_array[0] is item): # first
#         return sorted_array[0]
#     elif (sorted_array[-1] is item): # last
#         return sorted_array[-1]
    
#     while (found is not True):
#         midpoint = (len(sorted_array) -1) // 2
#         if (sorted_array[midpoint] == item):
#             found = True
#             print("found")
#         else:
#             # decide which direction to go to (left or right)
#             if sorted_array[midpoint] < item:
#                 midpoint -= 1 # go right
#             else:
#                 midpoint += 1 # go left

def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    left = 0
    right = len(array) -1

    while (left <= right): # loop through this as long as left & right are in the correct positions
        midpoint = (left + right) // 2
        if (array[midpoint] == item):
            return True
        elif (array[midpoint] < item):
            # go right
            right = midpoint - 1
        else:
            # go left
            left = midpoint + 1
    return None # not found

if __name__ == "__main__":
    my_array = [9,1,5,2,3,6,4,7,8,10]
    bin_search = binary_search_iterative(my_array, 6)
    print(bin_search)
