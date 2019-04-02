# Place to test code before implementing
def decode(digits, base):
    powers_of_two = [1,2,4,8,16,32,64,128,256]
    if base == 2:

        # we reverse the digits so we can count powers_of_two from left to right.
        reversed_digits = digits[::-1]

        indexs_of_ones = list()

        for index, value in enumerate(reversed_digits):
            if value == "1":
                indexs_of_ones.append(index)

        nums_to_add = list()

        for index, value in enumerate(powers_of_two):
            for item in indexs_of_ones:
                if index == item:
                    nums_to_add.append(value)

        return sum(nums_to_add)



if __name__ == "__main__":
    binary = decode("10", 2)
    print(binary)
