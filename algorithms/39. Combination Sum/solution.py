from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(i, current):
            if current == target:
                result.append(path.copy())
                return
            if i >= len(candidates) or current > target:
                return
            path.append(candidates[i])
            backtrack(i, current + candidates[i])
            path.pop()
            backtrack(i + 1, current)

        result, path = [], []
        backtrack(0, 0)
        return result


def test_combinationSum():
    solution = Solution()

    # Test case 1: Regular case with multiple combinations
    print("Test case 1: Regular case with multiple combinations")
    candidates = [2, 3, 6, 7]
    target = 7
    expected = [[2, 2, 3], [7]]
    result = solution.combinationSum(candidates, target)
    assert sorted(result) == sorted(expected), "Test case 1 failed"
    print("Passed")

    # Test case 2: Case with no combinations
    print("Test case 2: Case with no combinations")
    candidates = [2, 4, 6, 8]
    target = 5
    expected = []
    result = solution.combinationSum(candidates, target)
    assert result == expected, "Test case 2 failed"
    print("Passed")

    # Test case 3: Single element that is the target
    print("Test case 3: Single element that is the target")
    candidates = [7]
    target = 7
    expected = [[7]]
    result = solution.combinationSum(candidates, target)
    assert result == expected, "Test case 3 failed"
    print("Passed")

    # Test case 4: Single element that is less than the target
    print("Test case 4: Single element that is less than the target")
    candidates = [3]
    target = 9
    expected = [[3, 3, 3]]
    result = solution.combinationSum(candidates, target)
    assert result == expected, "Test case 4 failed"
    print("Passed")

    # Test case 5: Candidates with one element multiple times
    print("Test case 5: Candidates with one element multiple times")
    candidates = [2, 3, 5]
    target = 8
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    result = solution.combinationSum(candidates, target)
    assert sorted(result) == sorted(expected), "Test case 5 failed"
    print("Passed")

    # Test case 6: Empty candidates list
    print("Test case 6: Empty candidates list")
    candidates = []
    target = 7
    expected = []
    result = solution.combinationSum(candidates, target)
    assert result == expected, "Test case 6 failed"
    print("Passed")

    # Test case 7: Candidates list with one element
    print("Test case 7: Candidates list with one element")
    candidates = [1]
    target = 2
    expected = [[1, 1]]
    result = solution.combinationSum(candidates, target)
    assert result == expected, "Test case 7 failed"
    print("Passed")


if __name__ == "__main__":
    test_combinationSum()
