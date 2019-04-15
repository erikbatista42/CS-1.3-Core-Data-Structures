#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    if pattern == "": # empty string
        return True

    if len(pattern) == 1: 
        if pattern in text:
            return True
        else: 
            return False

    pattern_index = 0
    for char in text:
        if char == pattern[pattern_index]:
            pattern_index += 1
            if len(pattern) == pattern_index:
                return True
        elif len(pattern) == 2:
            pattern_index = 0
        else:
            pattern_index = 0
            pattern_index += 1
    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    if pattern == "":
        return 0

    text_index = 0
    pattern_index = 0
    for char in text:
        if char == pattern[pattern_index]:
            pattern_index += 1
            text_index += 1
            if pattern_index == len(pattern):
                text_index -= len(pattern)
                return text_index
        else:
            text_index += 1
            pattern_index = 0
            if char == pattern[pattern_index]:
                pattern_index += 1

    return None # not found
    

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    index_list = []
    if pattern == "":
        for i in range(0, len(text)):
            index_list.append(i)
        return index_list
    
    text_index = 0
    pattern_index = 0
    pattern_index_two = 0

    for char in text:
        if char == pattern[pattern_index]:
            pattern_index += 1
            text_index += 1
            if pattern_index == len(pattern):
                a = text_index - len(pattern)
                index_list.append(a)
                pattern_index = 0
        else:
            text_index += 1
            pattern_index = 0
            if char == pattern[pattern_index]:
                pattern_index += 1

    return index_list # not found



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
    print(find_all_indexes("bananas", "nas"))