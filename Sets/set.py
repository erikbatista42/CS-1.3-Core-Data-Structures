from set_hashtable import SetHashTable

class Set():

    def __init__(self, elements=None):
        self.table = SetHashTable()
        self.size = 0
       
    def contains(self, value):
        # return a boolean indicating whether element is in this set
        if value in self.table.items():
            return True
        else:
            return False
        # return self.table.contains(value)

    def add(self, value):
        # add element to this set, if not present already
        self.table.set(value)
        self.size = self.table.size 
            
    def remove(self, value):
        # remove element from this set, if present, or else raise KeyError
        self.table.delete(value)
        self.size = self.table.size

if __name__ == "__main__":
    set = Set()
    set.add("marian")
    set.add("bob")
    set.remove("marian")
    print(set.table)
   
    
    
  