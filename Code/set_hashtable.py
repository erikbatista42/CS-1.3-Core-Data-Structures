from linkedlist import LinkedList

class SetHashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __repr__(self):
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        return hash(key) % len(self.buckets)

    def load_factor(self):
        load_factor = self.size / len(self.buckets)
        return load_factor

    def keys(self):
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        # Collect all values in each of the buckets
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Count number of key-value entries in each of the buckets
        item_count = 0
        for bucket in self.buckets:
            item_count += bucket.length()
        return item_count

    def contains(self, key):
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        return entry is not None  # True or False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Return the given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def set(self, value):
        # Find the bucket the given key belongs in
        index = self._bucket_index(value)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == value)
        if entry is not None:  # Found
            # In this case, the given key's value is being updated
            # Remove the old key-value entry from the bucket first
            bucket.delete(entry)
            self.size -= 1
        # Insert the new key-value entry into the bucket in either case
        bucket.append((value))
        self.size += 1
        # TODO: Check if the load factor exceeds a threshold such as 0.75
        if self.load_factor() > 0.75:
            # TODO: If so, automatically resize to reduce the load factor
            self._resize()

    def delete(self, value):
        # Find the bucket the given key belongs in
        index = self._bucket_index(value)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value == value)
        if entry is not None:  # Found
            # Remove the key-value entry from the bucket
            bucket.delete(entry)
            self.size -= 1
        else:  # Not found
            raise KeyError('Value not found: {}'.format(value))

    def _resize(self, new_size=None):
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size
        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size == 0:
            new_size = len(self.buckets) / 2  # Half size

        # hold all key value pairs
        temp_entries = self.items() # O(n)
        # reinit our buckets and size 
        self.__init__(new_size) # O(2b) => O(b)
        # rehash them into new buckets
        for v in temp_entries:
            self.set(v)
        
    def clear(self):
        self.__init__() # remove all items in table 

