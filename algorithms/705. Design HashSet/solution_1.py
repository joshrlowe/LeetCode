"""
Solution to LeetCode 705: Design HashSet

This implementation handles collisions using open addressing.
"""

import unittest


def isPrime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def nextPrime(number: int) -> int:
    while True:
        if isPrime(number):
            return number
        number += 1


class MyHashSet:

    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.set = [None, None]

    def hash(self, key):
        return key % self.capacity

    def add(self, key: int) -> None:
        index = self.hash(key)

        while self.set[index] is not None and self.set[index] != key:
            index = (index + 1) % self.capacity

        if self.set[index] is None:
            self.size += 1
            self.set[index] = key

            if self.size > self.capacity // 2:
                self.rehash()

    def remove(self, key: int) -> None:
        index = self.hash(key)

        while self.set[index] is not None:
            if self.set[index] == key:
                self.set[index] = None
                self.size -= 1
                self.fixup(index)
                return
            index = (index + 1) % self.capacity

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        start_index = index

        while self.set[index] is not None:
            if self.set[index] == key:
                return True
            index = (index + 1) % self.capacity
            if index == start_index:
                return False
        return False

    def rehash(self) -> None:
        old_set = self.set
        self.capacity = nextPrime(self.capacity * 2)
        self.set = [None] * self.capacity
        self.size = 0

        for item in old_set:
            if item is not None:
                self.add(item)

    def fixup(self, start_index):
        index = (start_index + 1) % self.capacity
        while self.set[index] is not None:
            original_index = self.hash(self.set[index])
            if (
                index > start_index
                and (original_index <= start_index or original_index > index)
            ) or (
                index < start_index
                and (original_index <= start_index and original_index > index)
            ):
                self.set[start_index] = self.set[index]
                self.set[index] = None
                start_index = index
            index = (index + 1) % self.capacity


class TestMyHashSet(unittest.TestCase):

    def setUp(self):
        self.hash_set = MyHashSet()

    def test_add_contains(self):
        self.hash_set.add(1)
        self.hash_set.add(2)
        self.assertTrue(self.hash_set.contains(1))
        self.assertTrue(self.hash_set.contains(2))
        self.assertFalse(self.hash_set.contains(3))

    def test_remove(self):
        self.hash_set.add(1)
        self.hash_set.remove(1)
        self.assertFalse(self.hash_set.contains(1))

    def test_rehash(self):
        for i in range(20):
            self.hash_set.add(i)
        for i in range(20):
            self.assertTrue(self.hash_set.contains(i))

    def test_add_duplicate(self):
        self.hash_set.add(1)
        self.hash_set.add(1)
        self.assertTrue(self.hash_set.contains(1))

    def test_remove_nonexistent(self):
        self.hash_set.add(1)
        self.hash_set.remove(2)
        self.assertTrue(self.hash_set.contains(1))
        self.assertFalse(self.hash_set.contains(2))

    def test_complex_operations(self):
        self.hash_set.add(1)
        self.hash_set.add(2)
        self.hash_set.remove(1)
        self.assertFalse(self.hash_set.contains(1))
        self.assertTrue(self.hash_set.contains(2))
        self.hash_set.add(2)
        self.hash_set.remove(2)
        self.assertFalse(self.hash_set.contains(2))

    def test_fixup(self):
        for i in range(20):
            self.hash_set.add(i)
        self.hash_set.remove(10)
        self.assertFalse(self.hash_set.contains(10))
        for i in range(20):
            if i != 10:
                self.assertTrue(self.hash_set.contains(i))


if __name__ == "__main__":
    unittest.main()
