from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


def test_can_attend_meetings():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    intervals1 = [[0, 30], [5, 10], [15, 20]]
    expected1 = False
    result1 = solution.canAttendMeetings(intervals1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: No overlapping meetings
    print("Test Case 2: No overlapping meetings")
    intervals2 = [[7, 10], [2, 4]]
    expected2 = True
    result2 = solution.canAttendMeetings(intervals2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - No overlapping meetings Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Single meeting
    print("Test Case 3: Single meeting")
    intervals3 = [[5, 10]]
    expected3 = True
    result3 = solution.canAttendMeetings(intervals3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - Single meeting Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Meetings that touch but do not overlap
    print("Test Case 4: Meetings that touch but do not overlap")
    intervals4 = [[1, 5], [5, 10], [10, 15]]
    expected4 = True
    result4 = solution.canAttendMeetings(intervals4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - Meetings that touch but do not overlap Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Overlapping meetings
    print("Test Case 5: Overlapping meetings")
    intervals5 = [[1, 4], [2, 5], [7, 9]]
    expected5 = False
    result5 = solution.canAttendMeetings(intervals5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - Overlapping meetings Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: All day meetings
    print("Test Case 6: All day meetings")
    intervals6 = [[0, 24], [24, 48], [48, 72]]
    expected6 = True
    result6 = solution.canAttendMeetings(intervals6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - All day meetings Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Empty intervals list
    print("Test Case 7: Empty intervals list")
    intervals7 = []
    expected7 = True
    result7 = solution.canAttendMeetings(intervals7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Empty intervals list Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: Meetings with negative time
    print("Test Case 8: Meetings with negative time")
    intervals8 = [[-5, 0], [0, 5]]
    expected8 = True
    result8 = solution.canAttendMeetings(intervals8)
    assert (
        result8 == expected8
    ), f"Test Case 8 - Meetings with negative time Failed: Expected {expected8}, got {result8}"
    print("Passed")


if __name__ == "__main__":
    test_can_attend_meetings()
