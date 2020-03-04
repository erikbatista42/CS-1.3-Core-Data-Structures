#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    Best case: O(1) - if pattern is empty
    Worst case: O(n^2) - because that's how much find_all_indexes()"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if not pattern: return True # empty string
        
        # if len(pattern) == 1: 
        #     if pattern in text: return True
        #     else: return False

        # pattern_index = 0
        # for char in text:
        #     if char == pattern[pattern_index]:
        #         pattern_index += 1
        #         if len(pattern) == pattern_index: return True
        #     elif len(pattern) == 2: pattern_index = 0
        #     else:
        #         pattern_index = 0
        #         pattern_index += 1
        # return False

        # refactored code
        # O(text * pattern) time
        # O(n) space - we append all items 
    if find_index(text, pattern) == None: 
        return False
    return True


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if not pattern: return 0
    '''
    Best case: O(1) - if pattern is empty 
    Worst case: O(n^2) - because that's how much find_all_indexes()
    '''
    # text_index = 0
    # pattern_index = 0
    # for char in text:
    #     if char == pattern[pattern_index]:
    #         pattern_index += 1
    #         text_index += 1
    #         if pattern_index == len(pattern):
    #             text_index -= len(pattern) # starting index of pattern
    #             return text_index
    #     else:
    #         text_index += 1
    #         pattern_index = 0
    #         if char == pattern[pattern_index]:
    #             pattern_index += 1
    # return None # not found

    # refactored code
    result = find_all_indexes(text, pattern) # O(n^3)
    if len(result) > 0: 
        return result[0]
    return None

def find_all_indexes(text, pattern):
    '''
    Best case: O(n) - if pattern is empty, this means the whole text is a pattern so we generate every index
    Worst case: O(n^2) - because for each character in text we look at each character in the pattern.
   '''
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    index_list = []
    if pattern == "":
        return [x for x in range(len(text))] # index list 
    
    text_index = 0
    pattern_index = 0
    while_text_index = 0
    current_index = 0

    for char in text: 
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

    return index_list

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
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
    main()
