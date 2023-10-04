class HashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buckets = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = []
        for i, (existing_key, _) in enumerate(self.buckets[index]):
            if existing_key == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        if self.buckets[index] is not None:
            for existing_key, value in self.buckets[index]:
                if existing_key == key:
                    return value
        raise KeyError(f"Key not found: {key}")

    def remove(self, key):
        index = self._hash(key)
        if self.buckets[index] is not None:
            for i, (existing_key, _) in enumerate(self.buckets[index]):
                if existing_key == key:
                    del self.buckets[index][i]
                    return
        raise KeyError(f"Key not found: {key}")

    def display(self):
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: {bucket}")

# Example usage:
hash_map = HashMap()

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)

hash_map.display()

print("Get 'two':", hash_map.get("two"))

hash_map.remove("two")

hash_map.display()
