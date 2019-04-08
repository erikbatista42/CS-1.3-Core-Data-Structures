#!python

import string


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, "base is out of range: {}".format(base)
    lenOfNum = len(str(digits))
    total = 0
    hexMap = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    numAsList = list(str(digits))
    for num in numAsList:
        for key in hexMap.keys():
            if num is key:
                num = hexMap.get(key)
        lenOfNum -= 1
        total += int(num) * (base**lenOfNum)
    return total


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    hex_map = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
    result_list = []
    my_str = ""

    while (number != 0):
        whole_num = number // base
        remainder = number % base
        if (base is 16):
            for key in hex_map.keys():
                if key is remainder:
                    remainder = hex_map.get(key)
        result_list += [remainder]
        number = whole_num
    for num in result_list:
        my_str += str(num)
    my_str = my_str[::-1]
    return my_str


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    first_result = decode(digits, base1)
    final_result = encode(first_result, base2)
    return final_result


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if (len(args) == 3):
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == "__main__":
    # main()
    binary = encode(1, 2)
    print(binary)