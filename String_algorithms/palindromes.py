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
    # Best & Worse running time: O(n) because we're iterating n elements (I think) because we iterate n times, we search and insert
    new_text = []
    text_reversed = []
    lower_case_alphabet = string.ascii_lowercase

    # ignore all special characters
    for char in text.lower(): # O(n) => Looking through n elements
        if char in lower_case_alphabet: # search => O(n)
            text_reversed.insert(0, char) # insertion => O(n)
            new_text.append(char) # O(1)
        else:
            continue
    text_reversed = "".join(text_reversed)# O(n)? Iterating through text_reversed with n elements
    new_text = "".join(new_text) # O(n)? Iterating through new_text with n elements

    if text_reversed == new_text:
        return True # found
    return False # not found


def is_palindrome_recursive(text, left=None, right=None, new_text=None):
    # O(n*n) because we use the list comprehension to iterate n elements and function keeps calling itself until base conditions are called
    alphabet = string.ascii_lowercase
    # set new_text value
    if new_text == None:
        # list comprehension at new_text returns given text as a list with no special characters 
        return is_palindrome_recursive(text, left, right, [char for char in text.lower() if char in alphabet])

    # set left and right values
    if left == None and right == None:
        return is_palindrome_recursive(text, 0, len(new_text) -1, new_text)

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
    # print(is_palindrome_recursive("ABCZBA"))
    # print(string.punctuation)
    a = "erik2"
    print(frozenset(a))
