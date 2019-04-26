class Set():

    def __init__(self, elements=None):
        self.size = 0
        self.elements = elements
        if elements is not None: 
            for element in elements:
                self.add(element)
            
    def contains(self, element):
        # return a boolean indicating whether element is in this set
        if element in self.elements:
            return True
        else:
            return False

    def add(self, element):
        # add element to this set, if not present already
        if element not in self.elements:
            pass

    def remove(self, element):
        # remove element from this set, if present, or else raise KeyError
        pass

if __name__ == "__main__":
    set = Set(["A","B","C"])
    print(set.elements)
    
  