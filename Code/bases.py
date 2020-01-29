#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    # Decode digits from binary (base 2)
    # if base == 2:
    #     total_sum = 0
    #     for i, num in enumerate(reversed(digits)):
    #         if num == "1":
    #             total_sum += 2**i
    #     return total_sum
    # Decode digits from hexadecimal (base 16) + Decode digits from any base (2 up to 36)  
    hex_map = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}

    len_of_num = len(str(digits))
    total = 0
    
    num_as_list = list(str(digits))
    for num in num_as_list:
        for key in hex_map.keys():
            if num == key:
                num = hex_map.get(key)
        len_of_num -= 1
        total += int(num) * (base**len_of_num)
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
    # Encode number in binary (base 2)
    # if base == 2:
    #     output = ""
    #     while number != 0:
    #         # get remainder
    #         remainder = number % 2
    #         # divide number by 2 (base)
    #         number = number // base
    #         output += str(remainder)
            
    #     # return reversed ouput str
    #     return output[::-1]

    # Encode number in hexadecimal (base 16) + Encode number in any base (2 up to 36)
    base_16_up_to_36 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f", 16: "g", 17: "h", 18: "i", 19: "j", 20: "k", 21: "l", 22: "m", 23: "n", 24: "o", 25: "p", 26: "q", 27: "r", 28: "s", 29: "t", 30: "u", 31: "v", 32: "w", 33: "x", 34: "y", 35: "z", 36: 10}

    result_list = []
    my_str = ""

    while (number != 0):
        whole_num = number // base
        remainder = number % base

        remainder = base_16_up_to_36.get(remainder)

        if remainder in base_16_up_to_36:
            

        for key in base_16_up_to_36.keys():
            if key == remainder:
                remainder = base_16_up_to_36.get(key)

        result_list += [remainder]
        
        number = whole_num
    # print(result_list)
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
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()