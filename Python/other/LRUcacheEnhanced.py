"""
LRU Cache.

Lease Recently Used Cache.

Overview (Conditions):
1. The cache should have a maximum size, and should evict the least recently used item when the cache is full.

Operations:
Get(key) - Get the value of the key in the cache.
Put(key, value) - Put the value of the key in the cache if it is not already there.
Delete(key) - Delete the key from the cache.
Display - Display the cache in order of most recently used to least recently used.
"""
from collections import OrderedDict


class Lrucache:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        # Key is not in the cache
        if key not in self.cache:
            raise KeyError(f"Key {key} is not in the cache")
        # Key is in the cache
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # kye in the cache
        if key in self.cache:
            del self.cache[key]
        # Cache is full
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        # Add key to the cache
        self.cache[key] = value

    def delete(self, key: int) -> None:
        # key in not in the cache
        if key not in self.cache:
            raise KeyError(f"Key {key} is not in the cache")
        # key in the cache
        del self.cache[key]

    def resize(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("Capacity must be greater than 0")

        # If capacity is capacity is equal to the current capacity
        if capacity == self.capacity:
            print("Capacity is already equal to the current capacity")
            return

        # if capacity is less than the current capacity
        if capacity < self.capacity:
            for _ in range(self.capacity - capacity):
                self.cache.popitem(last=False)

        # Update the capacity
        self.capacity = capacity

    def display(self):
        return self.cache.items()


if __name__ == "__main__":
    cache = Lrucache(5)
    message = "LRU cache current state: {state}"
    cache.put(1, "apple")
    cache.put(2, "banana")
    cache.put(3, "cherry")
    cache.put(4, "pineapple")
    cache.put(5, "grape")

    # print(message.format(state=cache.display()))
    # target_value = cache.get(3)
    # print(f"Value of key 3: {target_value}")
    # cache.delete(2)
    # print(message.format(state=cache.display()))

    cache.resize(5)
    # cache.put(6, "kiwi")
    print(message.format(state=cache.display()))

# advices:
# O(n) - Delete the key from the cache.
# O(n) - Resize the cache.
# O(1) - Get the value of the key in the cache.
# O(1) - Put the value of the key in the cache if it is not already there.
# O(1) - Display the cache in order of most recently used to least recently used.
# O(1) - Delete the key from the cache.
