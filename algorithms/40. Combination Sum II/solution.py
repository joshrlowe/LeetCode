from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(start, curSum):
            if curSum == target:
                result.append(path.copy())
                return
            if curSum > target:
                return
            for i in range(start, len(candidates)):
                if i != start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                helper(i + 1, curSum + candidates[i])
                path.pop()

        candidates.sort()
        result, path = [], []
        helper(0, 0)
        return result


def test_combinationSum2():
    solution = Solution()

    # Test case 1: Regular case with multiple combinations
    print("Test case 1: Regular case with multiple combinations")
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    result = solution.combinationSum2(candidates, target)
    assert sorted(result) == sorted(expected), "Test case 1 failed"
    print("Passed")

    # Test case 2: No combinations possible
    print("Test case 2: No combinations possible")
    candidates = [2, 4, 6]
    target = 1
    expected = []
    result = solution.combinationSum2(candidates, target)
    assert result == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Single element equal to target
    print("Test case 3: Single element equal to target")
    candidates = [3]
    target = 3
    expected = [[3]]
    result = solution.combinationSum2(candidates, target)
    assert sorted(result) == sorted(expected), "Test case 3 failed"
    print("Passed")

    # Test case 4: Empty candidates list
    print("Test case 4: Empty candidates list")
    candidates = []
    target = 5
    expected = []
    result = solution.combinationSum2(candidates, target)
    assert result == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: All elements are the same
    print("Test case 5: All elements are the same")
    candidates = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    target = 2
    expected = [[1, 1]]
    result = solution.combinationSum2(candidates, target)
    assert sorted(result) == sorted(expected), "Test case 5 failed"
    print("Passed")

    # Test case 6: Target is larger than sum of all elements
    print("Test case 6: Target is larger than sum of all elements")
    candidates = [1, 2, 3]
    target = 10
    expected = []
    result = solution.combinationSum2(candidates, target)
    assert result == expected, "Test case 6 failed"
    print("Passed")


if __name__ == "__main__":
    test_combinationSum2()
