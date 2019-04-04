import string

def encode(digits, base):
    if base == 16:
        # hexadecimals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        hexadecimals = string.hexdigits
        new_digits_list = list()
        # new_digits = "".join(new_digits_list)

        for index,value in enumerate(hexadecimals):
            for digit in digits:
                if digit == value:
                    # print(index)
                    new_digits_list.append(index)

        # num_of_digits = len(digits)
        total = 0
        new_digits_len = len(new_digits_list)
        # print(new_digits_len)

        for digit in new_digits_list:
            # print(digit)
            new_digits_len -= 1
            total += int(digit) * (base**new_digits_len)

        return total

if __name__ == "__main__":
    #10,11,12
    # bead
    binary = encode("7e", 16)
    print(binary)


