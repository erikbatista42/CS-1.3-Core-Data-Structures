# Place to test code before implementing
def decode(digits, base):
    powers_of_two = [1,2,4,8,16,32,64,128,256]
    if base == 2:
        digits_list = list(digits)
        reversed_digits = digits[::-1] # so we can multiply from right to left

        all_nums = []
        all_indexs =[]

        for index, value in enumerate(reversed_digits):
            if value == "1":
                all_indexs.append(index)


        for index, value in enumerate(powers_of_two):
            for item in all_indexs:
                if index == item:
                    all_nums.append(value)
        return sum(all_nums)



if __name__ == "__main__":
    binary = decode("00111111", 2)
    print(binary)
