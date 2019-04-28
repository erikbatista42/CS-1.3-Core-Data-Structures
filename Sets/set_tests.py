from set import Set
import unittest

# tests for contain, add and remove
class SetTest(unittest.TestCase):
    def test_init(self):
        set = Set(["A","B","C"])
        assert set.elements == ["A","B","C"]
        assert set.size == 3
    
    def test_add(self):
        set = Set(["A","B","C"])
        set.add("D")
        set.add("E")
        assert set.contains("D")
        assert set.contains("E")
        assert set.size == 5

if __name__ == "__main__":
    unittest.main()