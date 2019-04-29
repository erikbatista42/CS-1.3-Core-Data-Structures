from set_hashtable import SetHashTable

class Set():

    def __init__(self, elements=None):
        self.elements = elements # instantiated elements for testing purposes
        self.table = SetHashTable()
        self.size = 0
        for item in elements:
            self.add(item)
       
    def __repr__(self):
        """Return a string representation of this set."""
        return 'Set({!r})'.format(self.table.items())

    def contains(self, value):
        # return a boolean indicating whether element is in this set
        if value in self.table.items():
            return True
        else:
            return False

    def add(self, value):
        if self.contains(value) is False:
            self.table.set(value)
            self.size = self.table.size 
                 
    def remove(self, value):
        # remove element from this set, if present, or else raise KeyError
        self.table.delete(value)
        self.size = self.table.size

    # set operations on other sets
    def union(self, other_set):
        """other_set: takes in another set
        Takes in a set and yields a set with all elements in both sets.
        Example: 
        set_one = ["sam","bob","joe"]
        set_two = ["sam", "bob", "marian","yo-yo"]
        output_set = ["sam", "bob","joe", "marian","yo-yo"]
        """
        for item in other_set.elements:
            self.add(item)
        return self
    
    def intersection(self, other_set):
        """other_set: takes in another set
        Takes in a set and yields a set with elements that are in both sets.
        Example: 
        set_one = ["sam","bob","joe"]
        set_two = ["sam", "bob", "marian","yo-yo"]
        output_set = ["sam", "bob"]
        """
        new_set = self
        new_set.table.clear()

        for item in other_set.elements:
            if item in self.elements:
                new_set.add(item)
        return new_set
    
    def difference(self, other_set):
        """
        Yields the difference betweens two sets. 
        or 
        all the elements in self that are not in the other_set
        -Example:
        self = ["M", "L", "A", "C", "Z", "W"]
        other_set = ["X", "N", "O", "L", "A", "M"]
        self - other_set = ["C", Z", "W"]
        """
        result_set = self
        result_set.table.clear()

        for item in self.elements:
            if item not in other_set.elements:
                result_set.add(item)
        return result_set
        
    
    def is_subset(self, other_set):
        # explanation
        pass


if __name__ == "__main__":
    set_one = Set(["M","L","A", "C", "Z","W"])
    set_two = Set(["X", "N", "O","L", "A", "M"])
    # print(set_two)
    # print(set_one.elements + set_two.elements)
    o = set_one.intersection(set_two)
    print(set_one.difference(set_two))

    
    
  