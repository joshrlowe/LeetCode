"""
LeetCode 706: Design HashMap

This solution uses chaining to handle collisions.
"""


class PairNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 0
        self.capacity = 10**4
        self.map = [PairNode(0, 0) for _ in range(10**4)]

    def hash(self, key):
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = PairNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[key % self.capacity]

        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[key % self.capacity]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


def test_my_hash_map():
    # Initialize a new hash map
    hash_map = MyHashMap()

    # Test put and get methods
    print("Test 1: Put and Get")
    hash_map.put(1, 1)
    hash_map.put(2, 2)
    assert hash_map.get(1) == 1, "Test 1 Failed: get(1) should return 1"
    assert hash_map.get(2) == 2, "Test 1 Failed: get(2) should return 2"
    assert hash_map.get(3) == -1, "Test 1 Failed: get(3) should return -1"
    print("Passed")

    # Test update value for an existing key
    print("Test 2: Update Value")
    hash_map.put(2, 1)
    assert hash_map.get(2) == 1, "Test 2 Failed: get(2) should return 1 after update"
    print("Passed")

    # Test remove method
    print("Test 3: Remove")
    hash_map.remove(2)
    assert hash_map.get(2) == -1, "Test 3 Failed: get(2) should return -1 after removal"
    print("Passed")

    # Test handling of collisions
    print("Test 4: Handle Collisions")
    hash_map.put(10**4, 3)
    hash_map.put(0, 4)
    assert hash_map.get(10**4) == 3, "Test 4 Failed: get(10**4) should return 3"
    assert hash_map.get(0) == 4, "Test 4 Failed: get(0) should return 4"
    hash_map.remove(10**4)
    assert (
        hash_map.get(10**4) == -1
    ), "Test 4 Failed: get(10**4) should return -1 after removal"
    print("Passed")


if __name__ == "__main__":
    test_my_hash_map()
