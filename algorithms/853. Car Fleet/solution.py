from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        stack = []
        for p, s in pos_speed:
            time = (target - p) / s
            if not stack or time > stack[-1][0]:
                stack.append([time, p])
        return len(stack)


def test_carFleet():
    solution = Solution()

    # Test Case 1: Normal case with multiple car fleets
    print("Test 1: Normal case with multiple car fleets")
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    expected = 3
    result = solution.carFleet(target, position, speed)
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("Test 1 Passed")

    # Test Case 2: All cars arrive together as a single fleet
    print("Test 2: All cars arrive together as a single fleet")
    target = 10
    position = [0, 2, 4]
    speed = [2, 2, 2]
    expected = 3
    result = solution.carFleet(target, position, speed)
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("Test 2 Passed")

    # Test Case 3: Each car is a separate fleet
    print("Test 3: Each car is a separate fleet")
    target = 100
    position = [0, 10, 20, 30, 40]
    speed = [10, 9, 8, 7, 6]
    expected = 1
    result = solution.carFleet(target, position, speed)
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("Test 3 Passed")

    # Test Case 4: Some cars form fleets, others do not
    print("Test 4: Some cars form fleets, others do not")
    target = 100
    position = [10, 20, 30, 40, 50]
    speed = [1, 2, 3, 4, 5]
    expected = 5
    result = solution.carFleet(target, position, speed)
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("Test 4 Passed")

    # Test Case 5: No cars
    print("Test 5: No cars")
    target = 10
    position = []
    speed = []
    expected = 0
    result = solution.carFleet(target, position, speed)
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("Test 5 Passed")

    # Test Case 6: Single car
    print("Test 6: Single car")
    target = 10
    position = [3]
    speed = [3]
    expected = 1
    result = solution.carFleet(target, position, speed)
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("Test 6 Passed")

    # Test Case 7: Two cars with same speed and different positions
    print("Test 7: Two cars with same speed and different positions")
    target = 12
    position = [6, 8]
    speed = [3, 3]
    expected = 2
    result = solution.carFleet(target, position, speed)
    assert result == expected, f"Test 7 Failed: expected {expected}, got {result}"
    print("Test 7 Passed")


if __name__ == "__main__":
    test_carFleet()
