from sets import Set
import unittest

# tests for contain, add and remove
class SetTest(unittest.TestCase):
    def test_init(self):
        set = Set(["A","B","C"])
        assert set.elements[1] == "B"


if __name__ == "__main__":
    unittest.main()