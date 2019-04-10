#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    new_text = []
    text_reversed = []
    lower_case_alphabet = string.ascii_lowercase

    # ignore all special characters
    for char in text.lower():
        if char in lower_case_alphabet:
            text_reversed.insert(0, char)
            new_text.append(char)
        else:
            continue
    text_reversed = "".join(text_reversed)
    new_text = "".join(new_text)

    if text_reversed == new_text:
        return True # found
    return False # not found

alphabet = string.ascii_lowercase
def is_palindrome_recursive(text, left=None, right=None, new_text=None):
    
    # set new_text value
    if new_text == None:
        # list comprehension at new_text returns text list with no special characters 
        return is_palindrome_recursive(text, left = None, right = None, new_text=[char for char in text.lower() if char in alphabet])
    # set left and right values
    if left == None and right == None:
        return is_palindrome_recursive(text, left = 0, right = len(new_text) -1, new_text = new_text)

    # if there are 2 items and are not the same 
    if len(new_text) -1 == 1 and new_text[left] != new_text[right]:
        return False

    # empty string or one char in text 
    if left > right or left == 0 and right == 0: 
        return True 
    
    if left + 1 == right and right -1 == left and new_text[left] == new_text[right]:
        return True 
    # both pointers are the same
    elif new_text[left] == new_text[right]:
        return is_palindrome_recursive(text, left +1, right -1, new_text)
    else:
        return False 



def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    # main()
    # print(is_palindrome_iterative("RaceCar"))
    print(is_palindrome_recursive("ABCZBA"))