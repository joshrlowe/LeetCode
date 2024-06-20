from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(i):
            if len(path) == k:
                result.append(path[:])
                return
            if i > n:
                return
            for j in range(i, n + 1):
                path.append(j)
                helper(j + 1)
                path.pop()

        result, path = [], []
        helper(1)
        return result


def test_combine():
    solution = Solution()

    # Test case 1: Regular case
    print("Test case 1: Regular case")
    n = 4
    k = 2
    expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    result = solution.combine(n, k)
    assert sorted(result) == sorted(expected), "Test case 1 failed"
    print("Passed")

    # Test case 2: k equals n
    print("Test case 2: k equals n")
    n = 3
    k = 3
    expected = [[1, 2, 3]]
    result = solution.combine(n, k)
    assert sorted(result) == sorted(expected), "Test case 2 failed"
    print("Passed")

    # Test case 3: k is 1
    print("Test case 3: k is 1")
    n = 4
    k = 1
    expected = [[1], [2], [3], [4]]
    result = solution.combine(n, k)
    assert sorted(result) == sorted(expected), "Test case 3 failed"
    print("Passed")

    # Test case 4: k is 0 (should return an empty list)
    print("Test case 4: k is 0")
    n = 4
    k = 0
    expected = [[]]
    result = solution.combine(n, k)
    assert sorted(result) == sorted(expected), "Test case 4 failed"
    print("Passed")

    # Test case 5: n is 1 and k is 1
    print("Test case 5: n is 1 and k is 1")
    n = 1
    k = 1
    expected = [[1]]
    result = solution.combine(n, k)
    assert sorted(result) == sorted(expected), "Test case 5 failed"
    print("Passed")

    # Test case 6: n is 5 and k is 3
    print("Test case 6: n is 5 and k is 3")
    n = 5
    k = 3
    expected = [
        [1, 2, 3],
        [1, 2, 4],
        [1, 2, 5],
        [1, 3, 4],
        [1, 3, 5],
        [1, 4, 5],
        [2, 3, 4],
        [2, 3, 5],
        [2, 4, 5],
        [3, 4, 5],
    ]
    result = solution.combine(n, k)
    assert sorted(result) == sorted(expected), "Test case 6 failed"
    print("Passed")


if __name__ == "__main__":
    test_combine()
