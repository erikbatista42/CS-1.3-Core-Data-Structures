import string
# Place to test code before implementing


def encode(number, base):
    hexMap = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}

    # base_25 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, "a": 10, "b": 11, "c", 12, "d": 13, "e": 14, "f": 15, "g": 16, "h": 17, "i": 18, "j": 19, "k": 20, "l": 21, "m": 22, "n": 23, "o": 24, 10: 25}

    base_25 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16, "h": 17, "i": 18, "j": 19, "k": 20, "l": 21, "m": 22, "n": 23, "o": 24, 10: 25}

    print(base_25)

        
    # resultList = []
    # myStr = ''
    # while (number != 0):
    #     wholeNum = number // base
    #     remainder = number % base
    #     if (base is 16):
    #         for key in hexMap.keys():
    #             if key is remainder:
    #                 remainder = hexMap.get(key)
    #     resultList += [remainder]
    #     number = wholeNum
    # for num in resultList:
    #     myStr += str(num)
    # myStr = myStr[::-1]
    # return myStr


if __name__ == "__main__":
    e = encode(123, 1)
    print(e)
