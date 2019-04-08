import string

def decode(digits, base):
    if base == 16:
        lenOfNum = len(str(digits))
        total = 0
        hexMap = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15 }
        numAsList = list(str(digits))
        for num in numAsList:
            # check if one of the digits is a char..if it is, the base is 16
            for key in hexMap.keys():
                if num is key:
                    # set the digit to be it's decimal value from the map
                    num = hexMap.get(key)
            # subtract 1 from the number length
            lenOfNum -= 1
            # multiply each digit in the list by base^lenOfNum and add it to
            # the running sum
            total += int(num) * (base**lenOfNum)
        return total
    else:
        num_of_digits = len(digits)
        total = 0

        for digit in digits:
            num_of_digits -= 1
            total += int(digit) * (base**num_of_digits)

        return total

if __name__ == "__main__":
    #10,11,12
    # bead
    binary = decode("a", 16)
    print(binary)


