
# from palindromes import is_palindrome_recursive
import string


if __name__ == "__main__":
    # is_palindrome_recursive("rAceCar")
    alphabet = string.ascii_lowercase
    # m = ["r","a","c","e","c","a","r","1"]
    # m = "".join(m)
    k = "RaCecAr1$%2342342342;:]{=+".lower()
    h = [char for char in k if char in alphabet]
    print(h)
    # a = str.translate(m, alphabet)
    # print(a)