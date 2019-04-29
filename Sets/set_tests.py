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
    
    def test_remove(self):
        set = Set(["A","B","C"])
        set.remove("C")
        set.remove("B")
        assert set.size == 1
        assert set.contains("B") == False
    
    def test_contains(self):
        set = Set(["A","B","C"])
        # actually containing
        assert set.contains("A") == True
        assert set.contains("B") == True
        assert set.contains("C") == True
        # not containing 
        assert set.contains("D") == False
        assert set.contains("E") == False

    def test_union(self):
        set_one = Set(["A","B","C"])
        set_two = Set(["A","B","C","E","F","G"])
        union = set_one.union(set_two)
        assert union.contains("A") == True
        assert union.contains("B") == True
        assert union.contains("C") == True
        assert union.contains("E") == True
        assert union.contains("F") == True
        assert union.contains("G") == True
        assert union.size == 6


if __name__ == "__main__":
    unittest.main()