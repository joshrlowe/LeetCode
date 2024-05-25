from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            match (op):
                case "+":
                    scores.append(scores[-1] + scores[-2])
                case "D":
                    scores.append(scores[-1] * 2)
                case "C":
                    scores.pop()
                case _:
                    scores.append(int(op))

        return sum(scores)


def test_cal_points():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    operations1 = ["5", "2", "C", "D", "+"]
    expected1 = 30
    result1 = solution.calPoints(operations1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: All operations types
    print("Test Case 2: All operations types")
    operations2 = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    expected2 = 27
    result2 = solution.calPoints(operations2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - All operations types Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Multiple cancellations
    print("Test Case 3: Multiple cancellations")
    operations3 = ["1", "C", "2", "C", "3", "C"]
    expected3 = 0
    result3 = solution.calPoints(operations3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - Multiple cancellations Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Single "D" operation
    print("Test Case 4: Single 'D' operation")
    operations5 = ["5", "D"]
    expected5 = 15
    result5 = solution.calPoints(operations5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - Single 'D' operation Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 5: Single "C" operation
    print("Test Case 5: Single 'C' operation")
    operations6 = ["5", "2", "C"]
    expected6 = 5
    result6 = solution.calPoints(operations6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - Single 'C' operation Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 6: Empty operations list
    print("Test Case 6: Empty operations list")
    operations7 = []
    expected7 = 0
    result7 = solution.calPoints(operations7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Empty operations list Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 7: All positive scores
    print("Test Case 7: All positive scores")
    operations8 = ["5", "3", "7", "D", "+"]
    expected8 = 50
    result8 = solution.calPoints(operations8)
    assert (
        result8 == expected8
    ), f"Test Case 8 - All positive scores Failed: Expected {expected8}, got {result8}"
    print("Passed")


if __name__ == "__main__":
    test_cal_points()
