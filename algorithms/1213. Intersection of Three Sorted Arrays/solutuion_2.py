from typing import List


class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]
    ) -> List[int]:
        def find_sub_intersection(a1, a2):
            i, j = 0, 0
            result = []
            while i < len(a1) and j < len(a2):
                if a1[i] < a2[j]:
                    i += 1
                elif a1[i] > a2[j]:
                    j += 1
                else:
                    result.append(a1[i])
                    i += 1
                    j += 1
            return result

        arr1_arr2 = find_sub_intersection(arr1, arr2)
        return find_sub_intersection(arr1_arr2, arr3)


def test_arrays_intersection():
    solution = Solution()

    # Test Case 1: Basic functionality test
    print("Test Case 1: Basic functionality test")
    arr1_1 = [1, 2, 3, 4, 5]
    arr2_1 = [1, 2, 5, 7, 9]
    arr3_1 = [1, 3, 4, 5, 8]
    expected1 = [1, 5]
    result1 = solution.arraysIntersection(arr1_1, arr2_1, arr3_1)
    assert (
        result1 == expected1
    ), f"Test Case 1 - Basic functionality test Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: No common elements
    print("Test Case 2: No common elements")
    arr1_2 = [1, 2, 3]
    arr2_2 = [4, 5, 6]
    arr3_2 = [7, 8, 9]
    expected2 = []
    result2 = solution.arraysIntersection(arr1_2, arr2_2, arr3_2)
    assert (
        result2 == expected2
    ), f"Test Case 2 - No common elements Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: All elements are common
    print("Test Case 3: All elements are common")
    arr1_3 = [1, 2, 3]
    arr2_3 = [1, 2, 3]
    arr3_3 = [1, 2, 3]
    expected3 = [1, 2, 3]
    result3 = solution.arraysIntersection(arr1_3, arr2_3, arr3_3)
    assert (
        result3 == expected3
    ), f"Test Case 3 - All elements are common Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Some elements are common
    print("Test Case 4: Some elements are common")
    arr1_4 = [1, 2, 3, 4, 5]
    arr2_4 = [2, 4, 6, 8]
    arr3_4 = [1, 2, 3, 4, 5, 6]
    expected4 = [2, 4]
    result4 = solution.arraysIntersection(arr1_4, arr2_4, arr3_4)
    assert (
        result4 == expected4
    ), f"Test Case 4 - Some elements are common Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Empty arrays
    print("Test Case 5: Empty arrays")
    arr1_5 = []
    arr2_5 = []
    arr3_5 = []
    expected5 = []
    result5 = solution.arraysIntersection(arr1_5, arr2_5, arr3_5)
    assert (
        result5 == expected5
    ), f"Test Case 5 - Empty arrays Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: Arrays of different lengths
    print("Test Case 6: Arrays of different lengths")
    arr1_6 = [1, 2, 3, 4, 5, 6]
    arr2_6 = [2, 4, 6]
    arr3_6 = [1, 2, 3, 4]
    expected6 = [2, 4]
    result6 = solution.arraysIntersection(arr1_6, arr2_6, arr3_6)
    assert (
        result6 == expected6
    ), f"Test Case 6 - Arrays of different lengths Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Arrays with negative numbers
    print("Test Case 7: Arrays with negative numbers")
    arr1_7 = [-3, -2, -1, 0, 1, 2]
    arr2_7 = [-2, 0, 2]
    arr3_7 = [-3, -2, 2, 3]
    expected7 = [-2, 2]
    result7 = solution.arraysIntersection(arr1_7, arr2_7, arr3_7)
    assert (
        result7 == expected7
    ), f"Test Case 7 - Arrays with negative numbers Failed: Expected {expected7}, got {result7}"
    print("Passed")


if __name__ == "__main__":
    test_arrays_intersection()
