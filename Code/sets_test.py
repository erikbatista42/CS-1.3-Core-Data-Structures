from sets import Set
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
    
    def test_intersection(self):
        set_one = Set(["sam","bob","joe"])
        set_two = Set(["sam","bob","marian","yo-yo"])
        intersection = set_one.intersection(set_two) 
        assert intersection.contains("sam") == True
        assert intersection.contains("bob") == True
        assert intersection.contains("joe") == False
        assert intersection.contains("marian") == False
    
    def test_difference(self):
        set_one = Set(["M", "L", "A", "C", "Z", "W"])
        set_two = Set(["X", "N", "O", "L", "A", "M"])
        difference = set_one.difference(set_two)
        assert difference.contains("C") == True
        assert difference.contains("Z") == True
        assert difference.contains("W") == True
        assert difference.contains("A") == False
        assert difference.contains("O") == False

    def test_is_subset(self):
        set_one = Set(["A","B","C"])
        set_two = Set(["A","B","C","E","F","G"])
        set_three = Set(["A","B","C","D"])
        # true subsets
        assert set_one.is_subset(set_three) == True
        assert set_one.is_subset(set_two) == True
        assert set_one.is_subset(set_three) == True
        # false subsets
        assert set_two.is_subset(set_three) == False
        assert set_two.is_subset(set_one) == False
        assert set_three.is_subset(set_two) == False



if __name__ == "__main__":
    unittest.main()