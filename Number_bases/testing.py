import string
# Place to test code before implementing
def decode(digits, base):
#     powers_of_two = [1,2,4,8,16,32,64,128,256]
#     if base == 2:

#         # we reverse the digits so we can count powers_of_two from left to right.
#         reversed_digits = digits[::-1]

#         indexs_of_ones = list()

#         for index, value in enumerate(reversed_digits):
#             if value == "1":
#                 indexs_of_ones.append(index)

#         nums_to_add = list()

#         for index, value in enumerate(powers_of_two):
#             for item in indexs_of_ones:
#                 if index == item:
#                     nums_to_add.append(value)

#         return sum(nums_to_add)

    if base == 16:
        #hex
        hexadecimals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        #bin (1-16)
        # binaries = [0000,0001,0010,0011,0100,0101,0110,0111,1000,1001,1010,1011,1100,1101,1110,1111]

        # decimals = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

        powers_of_sixteen = [1,16,16**2,16**3,16**4,16**5,16**6,16**7,16**8,16**9,16**10]

        indexs_of_digits = list()
        calculated_digits = list()

        for index, value in enumerate(hexadecimals):
            for item in digits:
                if value == item: # if them_digit's item is d => True
                    indexs_of_digits.append(index)
        # print(indexs_of_digits)

        reversed_digits = indexs_of_digits[::-1]

        print(reversed_digits)

        for i in reversed_digits:
            for j in powers_of_sixteen:
                    # print(i*j)
                    # pass
                calculated_digits.append(i*j)


        return sum(calculated_digits) # decimal num

# def decode(digits, base):
#         # Handle up to base 36 [0-9a-z]
#     assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

#     hexadecimals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

#     decimals = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

#     if base == 16:
#         # turn all digits into nums
#         for i in hexadecimals:
#             for d in digits:
#                 if i

#     # Let n be the number of digits in the number. For example, 104 has 3 digits, so n=3.
#     n = len(digits)
#     # Let b be the base of the number. For example, 104 is decimal so b = 10.
#     b = base
#     # Let s be a running total, initially 0.
#     s = 0

#     # For each digit in the number, working left to right do:
#     for digit in digits:
#         # Subtract 1 from n.
#         n -= 1
#         # Multiply the digit times bn and add it to s.
#                 # (10*3) => 30
#         s += int(digit) * (b**n)

#     return s

def encode(number, base):
    if base == 16:
        print("base 16...oh nah!")
    else:
        n = number
        m = int()# Let m be the number, initially empty, that we are converting to. We'll be composing it right to left.
        b = base

        for i in n:


if __name__ == "__main__":
    binary = decode("7E", 16)
    print(binary)

