#!python

def contains(text, pattern):
    # Best Case: # O(n) - if there is no pattern. Don't have to iterate if the pattern is empty. So returning False
    # Worst Case: # O(n^3) - if there is a pattern and we have to loop through the whole thing n^3 times
    """Return a boolean indicating whether pattern occurs in text."""
    # if pattern == "": # empty string
    #     return True

    # if len(pattern) == 1: 
    #     if pattern in text:
    #         return True
    #     else: 
    #         return False

    # pattern_index = 0
    # for char in text:
    #     if char == pattern[pattern_index]:
    #         pattern_index += 1
    #         if len(pattern) == pattern_index:
    #             return True
    #     elif len(pattern) == 2:
    #         pattern_index = 0
    #     else:
    #         pattern_index = 0
    #         pattern_index += 1
    # return False
    if find_index(text, pattern) == None: # O(n^3)
        return False
    else:
        return True

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    # Best Case: # O(1) - if pattern is empty!
    # Worst Case: # O(n^3) - because calling find_all_indexes function
    if pattern == "":
        return 0

    # text_index = 0
    # pattern_index = 0
    # for char in text:
    #     if char == pattern[pattern_index]:
    #         pattern_index += 1
    #         text_index += 1
    #         if pattern_index == len(pattern):
    #             text_index -= len(pattern)
    #             return text_index
    #     else:
    #         text_index += 1
    #         pattern_index = 0
    #         if char == pattern[pattern_index]:
    #             pattern_index += 1

    # return None # not found
    result = find_all_indexes(text, pattern) # O(n^3)
    if len(result) > 0: # O(1) to check length
        return result[0]
    else: 
        return None# O(1)

    

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    # Best + Worst Case: # O(n^3) - Because we have 3 loops and have to make n^3 iterations. 
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    index_list = []
    if pattern == "":
        for i in range(0, len(text)): # O(n) because it loops n times
            index_list.append(i) # O(1)
        return index_list
    
    text_index = 0
    pattern_index = 0
    while_text_index = 0
    current_index = 0

    for char in text: # O(n) looping through each character in given text
        if char == pattern[pattern_index]:
            current_index = text_index
            print(while_text_index < len(text) -1)
            while while_text_index <= len(text) -1 and text[while_text_index] == pattern[pattern_index]: # O(n) because we're doing something n times until a condition is met.
                
                pattern_index += 1
                text_index += 1
                while_text_index += 1

                if pattern_index == len(pattern):
                    actual_index_start = text_index - len(pattern)
                    index_list.append(actual_index_start)
                    break

            text_index = current_index + 1
            pattern_index = 0
            while_text_index = current_index + 1


        else:
            text_index += 1       
            pattern_index = 0
            while_text_index += 1
            # if char == pattern[pattern_index]:
            #     pattern_index += 1

    return index_list



def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    # main()
    # print(find_all_indexes("abc", "cc"))
    # 10 a
    print(find_all_indexes("aaaaaaaaaa", "aaa"))