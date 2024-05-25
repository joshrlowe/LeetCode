from collections import deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students, sandwiches = deque(students), deque(sandwiches)
        turns = 0

        while students and turns < len(students):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                turns = 0
            else:
                students.rotate()
                turns += 1
        return len(students)


def test_count_students():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    students1 = [1, 1, 0, 0]
    sandwiches1 = [0, 1, 0, 1]
    assert (
        solution.countStudents(students1, sandwiches1) == 0
    ), "Test Case 1 - Basic functionality test Failed"
    print("Passed")

    # Test Case 2: All students get their preferred sandwiches
    print("Test Case 2: All students get their preferred sandwiches")
    students2 = [1, 0, 1, 0]
    sandwiches2 = [0, 1, 0, 1]
    assert (
        solution.countStudents(students2, sandwiches2) == 0
    ), "Test Case 2 - All students get their preferred sandwiches Failed"
    print("Passed")

    # Test Case 3: None of the students can get their preferred sandwiches
    print("Test Case 3: None of the students can get their preferred sandwiches")
    students3 = [1, 1, 1, 1]
    sandwiches3 = [0, 0, 0, 0]
    assert (
        solution.countStudents(students3, sandwiches3) == 4
    ), "Test Case 3 - None of the students can get their preferred sandwiches Failed"
    print("Passed")

    # Test Case 4: Some students cannot get their preferred sandwiches
    print("Test Case 4: Some students cannot get their preferred sandwiches")
    students4 = [1, 1, 0, 0]
    sandwiches4 = [1, 0, 0, 1]
    assert (
        solution.countStudents(students4, sandwiches4) == 0
    ), "Test Case 4 - Some students cannot get their preferred sandwiches Failed"
    print("Passed")

    # Test Case 5: One student prefers a different sandwich
    print("Test Case 5: One student prefers a different sandwich")
    students5 = [0, 0, 0, 1]
    sandwiches5 = [1, 0, 0, 1]
    assert (
        solution.countStudents(students5, sandwiches5) == 1
    ), "Test Case 5 - One student prefers a different sandwich Failed"
    print("Passed")

    # Test Case 6: Alternating preferences
    print("Test Case 6: Alternating preferences")
    students6 = [0, 1, 0, 1, 0]
    sandwiches6 = [1, 0, 1, 0, 1]
    assert (
        solution.countStudents(students6, sandwiches6) == 1
    ), "Test Case 6 - Alternating preferences Failed"
    print("Passed")

    # Test Case 7: No students
    print("Test Case 7: No students")
    students7 = []
    sandwiches7 = []
    assert (
        solution.countStudents(students7, sandwiches7) == 0
    ), "Test Case 7 - No students Failed"
    print("Passed")

    # Test Case 8: Single student, matching preference
    print("Test Case 8: Single student, matching preference")
    students8 = [0]
    sandwiches8 = [0]
    assert (
        solution.countStudents(students8, sandwiches8) == 0
    ), "Test Case 8 - Single student, matching preference Failed"
    print("Passed")

    # Test Case 9: Single student, mismatching preference
    print("Test Case 9: Single student, mismatching preference")
    students9 = [0]
    sandwiches9 = [1]
    assert (
        solution.countStudents(students9, sandwiches9) == 1
    ), "Test Case 9 - Single student, mismatching preference Failed"
    print("Passed")

    # Test Case 10: All students can get their sandwiches
    print("Test Case 10: All students can get their sandwiches")
    students10 = [0, 1, 1, 0, 0]
    sandwiches10 = [0, 1, 1, 0, 0]
    assert (
        solution.countStudents(students10, sandwiches10) == 0
    ), "Test Case 10 - All students can get their sandwiches Failed"
    print("Passed")

    # Additional Test Case 11: Some students cannot get their preferred sandwiches
    print("Test Case 11: Some students cannot get their preferred sandwiches")
    students11 = [1, 1, 1, 0, 0, 1]
    sandwiches11 = [1, 0, 0, 0, 1, 1]
    assert (
        solution.countStudents(students11, sandwiches11) == 3
    ), "Test Case 11 - Some students cannot get their preferred sandwiches Failed"
    print("Passed")

    # Additional Test Case 12: Mixed preferences with multiple students unable to eat
    print("Test Case 12: Mixed preferences with multiple students unable to eat")
    students12 = [1, 0, 0, 1, 1, 0, 1, 0]
    sandwiches12 = [0, 1, 0, 1, 0, 0, 0, 0]
    assert (
        solution.countStudents(students12, sandwiches12) == 2
    ), "Test Case 12 - Mixed preferences with multiple students unable to eat Failed"
    print("Passed")


if __name__ == "__main__":
    test_count_students()
