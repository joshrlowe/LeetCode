from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i):
            if i == len(nums):
                return [[]]

            res = []
            perms = helper(i + 1)
            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = p[:]
                    pCopy.insert(j, nums[i])
                    res.append(pCopy)
            return res

        return helper(0)


def test_permute():
    solution = Solution()

    # Test case 1: Regular case with multiple elements
    print("Test case 1: Regular case with multiple elements")
    nums = [1, 2, 3]
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    result = solution.permute(nums)
    assert sorted(result) == sorted(expected), "Test case 1 failed"
    print("Passed")

    # Test case 2: Single element
    print("Test case 2: Single element")
    nums = [1]
    expected = [[1]]
    result = solution.permute(nums)
    assert sorted(result) == sorted(expected), "Test case 2 failed"
    print("Passed")

    # Test case 3: Empty list
    print("Test case 3: Empty list")
    nums = []
    expected = [[]]
    result = solution.permute(nums)
    assert sorted(result) == sorted(expected), "Test case 3 failed"
    print("Passed")

    # Test case 4: Two elements
    print("Test case 4: Two elements")
    nums = [0, 1]
    expected = [[0, 1], [1, 0]]
    result = solution.permute(nums)
    assert sorted(result) == sorted(expected), "Test case 4 failed"
    print("Passed")

    # Test case 5: Duplicate elements (though the prompt implies no duplicates)
    print("Test case 5: Duplicate elements")
    nums = [1, 1]
    expected = [[1, 1], [1, 1]]
    result = solution.permute(nums)
    assert sorted(result) == sorted(expected), "Test case 5 failed"
    print("Passed")


if __name__ == "__main__":
    test_permute()
