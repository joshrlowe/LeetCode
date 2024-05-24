class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, val: int):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


def test_lru_cache():
    # Test case 1: Basic functionality
    print("Test case 1: Basic functionality")
    cache = LRUCache(2)  # Capacity of 2
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # Returns 1
    cache.put(3, 3)  # Evicts key 2
    assert cache.get(2) == -1  # Returns -1 (not found)
    cache.put(4, 4)  # Evicts key 1
    assert cache.get(1) == -1  # Returns -1 (not found)
    assert cache.get(3) == 3  # Returns 3
    assert cache.get(4) == 4  # Returns 4
    print("Passed")

    # Test case 2: Overwriting existing key
    print("Test case 2: Overwriting existing key")
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(1, 10)  # Overwrite key 1
    assert cache.get(1) == 10  # Returns 10
    print("Passed")

    # Test case 3: Capacity 1
    print("Test case 3: Capacity 1")
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)  # Evicts key 1
    assert cache.get(1) == -1  # Returns -1 (not found)
    assert cache.get(2) == 2  # Returns 2
    print("Passed")

    # Test case 4: Zero capacity
    print("Test case 4: Zero capacity")
    cache = LRUCache(0)
    cache.put(1, 1)  # Should not store anything
    assert cache.get(1) == -1  # Returns -1 (not found)
    print("Passed")

    # Test case 5: Access order affects eviction
    print("Test case 5: Access order affects eviction")
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)  # Access key 1
    cache.put(3, 3)  # Evicts key 2
    assert cache.get(2) == -1  # Returns -1 (not found)
    assert cache.get(1) == 1  # Returns 1
    assert cache.get(3) == 3  # Returns 3
    print("Passed")


if __name__ == "__main__":
    test_lru_cache()
