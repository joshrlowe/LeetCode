from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(partial, i):
            if i == len(nums):
                return res.append(partial[:])

            partial.append(nums[i])
            helper(partial, i + 1)
            partial.pop()
            helper(partial, i + 1)

        res, partial = [], []
        helper(partial, 0)
        return res


def run_test_case(test_case_num, nums, expected):
    solution = Solution()
    result = solution.subsets(nums)
    assert sorted(result) == sorted(
        expected
    ), f"Test case {test_case_num} failed: expected {expected}, got {result}"
    print(f"Test case {test_case_num} - Passed")


def test_subsets():
    # Test case 1: No elements
    print("Test case 1: No elements")
    run_test_case(1, [], [[]])

    # Test case 2: One element
    print("Test case 2: One element")
    run_test_case(2, [1], [[], [1]])

    # Test case 3: Two elements
    print("Test case 3: Two elements")
    run_test_case(3, [1, 2], [[], [1], [2], [1, 2]])

    # Test case 4: Three elements
    print("Test case 4: Three elements")
    run_test_case(4, [1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])

    # Test case 5: Four elements
    print("Test case 5: Four elements")
    run_test_case(
        5,
        [1, 2, 3, 4],
        [
            [],
            [1],
            [2],
            [1, 2],
            [3],
            [1, 3],
            [2, 3],
            [1, 2, 3],
            [4],
            [1, 4],
            [2, 4],
            [1, 2, 4],
            [3, 4],
            [1, 3, 4],
            [2, 3, 4],
            [1, 2, 3, 4],
        ],
    )

    # Test case 6: Negative and positive elements
    print("Test case 6: Negative and positive elements")
    run_test_case(
        6, [-1, 0, 1], [[], [-1], [0], [-1, 0], [1], [-1, 1], [0, 1], [-1, 0, 1]]
    )


if __name__ == "__main__":
    test_subsets()
