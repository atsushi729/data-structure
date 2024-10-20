# LRU cache implementation
# LRU - Least Recently Used

# Overview:
# The cache should have a maximum size, and should evict the least recently used item when the cache is full.
# The cache should be able to be initialized with a maximum size.
# class should be initialized with a maximum size.
# The cache should have a get method that returns the value associated with the key that is passed in.

# Actions:
# 1. If the key is not in the cache, return None.
# 2. Get the value of the key in the cache.
# 3. put the value of the key in the cache if it is not already there.
# 4. Display the cache in order of most recently used to least recently used.

from collections import OrderedDict


class LRUcache:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return None
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def delete(self, key: int) -> None:
        if key not in self.cache:
            return None
        if key in self.cache:
            del self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

    def display(self):
        print(self.cache.items())


if __name__ == "__main__":
    message = "LRU cache current state: {state}"
    cache = LRUcache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.display()
    current_state = cache.get(1)
    print(message.format(state=current_state))
    cache.display()
    cache.put(3, 3)
    cache.display()
    cache.delete(2)
    cache.display()