# A web app needs to redact some words. Write a function that takes two arrays of words(strings), and returns an array of words in the first array that are not in the second array.

# STEP 0 - pseudocode to plan how you will structure your soluction and run it on test case.

class Redact():
    def __init__(self):
        pass

    def redact(self, words, banned_words):
        result = []
        for word in words:
            if word not in banned_words:
                result.append(word)
            else: # in banned words
                banned_words.remove(word)
        return result

import unittest
class RedactTest(unittest.TestCase):
    def test_redact_uniques(self):
        array_one = ["erik", "bob", "joe", "larson"]
        array_two = ["erik", "nar", "larson", "ana"]
        re = Redact()
        redact = re.redact(array_one, array_two)
        assert redact == ["bob", "joe"]
    
    def test_redact_duplicates(self):
        array_one = ["erik", "bob", "joe", "larry", "erik"]
        array_two = ["erik", "nar", "larry", "ana", "nar"]
        re = Redact()
        redact = re.redact(array_one, array_two)
        assert redact == ["bob", "joe", "erik"]

    def test_redact_duplicates_two(self):
        array_one = ["erik", "bob", "joe", "larry", "erik", "john", "yo-yo", "yo-yo"]
        array_two = ["erik", "nar", "larry", "ana", "nar", "fe", "fe", "yo-yo"]
        re = Redact()
        redact = re.redact(array_one, array_two)
        assert redact == ["bob", "joe", "erik", "john", "yo-yo"]
if __name__ == "__main__":
    unittest.main()
    