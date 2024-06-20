from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs():
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    dfs()
                    count[n] += 1
                    perm.pop()

        result, perm = [], []
        count = Counter(nums)
        dfs()
        return result


def test_permuteUnique():
    solution = Solution()

    # Test case 1: Regular case with duplicates
    print("Test case 1: Regular case with duplicates")
    nums = [1, 1, 2]
    expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    result = solution.permuteUnique(nums)
    assert sorted(result) == sorted(expected), "Test case 1 failed"
    print("Passed")

    # Test case 2: No duplicates
    print("Test case 2: No duplicates")
    nums = [1, 2, 3]
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    result = solution.permuteUnique(nums)
    assert sorted(result) == sorted(expected), "Test case 2 failed"
    print("Passed")

    # Test case 3: Single element
    print("Test case 3: Single element")
    nums = [1]
    expected = [[1]]
    result = solution.permuteUnique(nums)
    assert result == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: Empty list
    print("Test case 4: Empty list")
    nums = []
    expected = [[]]
    result = solution.permuteUnique(nums)
    assert result == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: All elements are the same
    print("Test case 5: All elements are the same")
    nums = [2, 2, 2]
    expected = [[2, 2, 2]]
    result = solution.permuteUnique(nums)
    assert result == expected, "Test case 5 failed"
    print("Passed")


if __name__ == "__main__":
    test_permuteUnique()
