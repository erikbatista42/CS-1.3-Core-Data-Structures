import string
# Place to test code before implementing


def encode(number, base):
    hexMap = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}

    resultList = []
    myStr = ''
    while (number != 0):
        wholeNum = number // base
        remainder = number % base
        if (base is 16):
            for key in hexMap.keys():
                if key is remainder:
                    remainder = hexMap.get(key)
        resultList += [remainder]
        number = wholeNum
    for num in resultList:
        myStr += str(num)
    myStr = myStr[::-1]
    return myStr


if __name__ == "__main__":
    e = encode(123, 1)
    print(e)
