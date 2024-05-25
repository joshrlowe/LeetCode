from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        solution = []
        text_list = text.split()
        for i in range(len(text_list) - 2):
            if text_list[i] == first and text_list[i + 1] == second:
                solution.append(text_list[i + 2])
        return solution


def test_find_ocurrences():
    solution = Solution()

    # Test Case 1: Basic functionality
    print("Test Case 1: Basic functionality")
    text1 = "alice is a good girl she is a good student"
    first1, second1 = "a", "good"
    expected1 = ["girl", "student"]
    result1 = solution.findOcurrences(text1, first1, second1)
    assert (
        result1 == expected1
    ), f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Passed")

    # Test Case 2: No occurrences
    print("Test Case 2: No occurrences")
    text2 = "we will we will rock you"
    first2, second2 = "we", "are"
    expected2 = []
    result2 = solution.findOcurrences(text2, first2, second2)
    assert (
        result2 == expected2
    ), f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Passed")

    # Test Case 3: Multiple occurrences
    print("Test Case 3: Multiple occurrences")
    text3 = "we will we will rock you we will"
    first3, second3 = "we", "will"
    expected3 = ["we", "rock"]
    result3 = solution.findOcurrences(text3, first3, second3)
    assert (
        result3 == expected3
    ), f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Passed")

    # Test Case 4: Occurrence at the end of text
    print("Test Case 4: Occurrence at the end of text")
    text4 = "I love eating ice cream"
    first4, second4 = "ice", "cream"
    expected4 = []
    result4 = solution.findOcurrences(text4, first4, second4)
    assert (
        result4 == expected4
    ), f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Passed")

    # Test Case 5: Single occurrence
    print("Test Case 5: Single occurrence")
    text5 = "she sells sea shells by the sea shore"
    first5, second5 = "sea", "shells"
    expected5 = ["by"]
    result5 = solution.findOcurrences(text5, first5, second5)
    assert (
        result5 == expected5
    ), f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Passed")

    # Test Case 6: First and second words are the same
    print("Test Case 6: First and second words are the same")
    text6 = "we we are the champions"
    first6, second6 = "we", "we"
    expected6 = ["are"]
    result6 = solution.findOcurrences(text6, first6, second6)
    assert (
        result6 == expected6
    ), f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Passed")

    # Test Case 7: Empty text
    print("Test Case 7: Empty text")
    text7 = ""
    first7, second7 = "a", "b"
    expected7 = []
    result7 = solution.findOcurrences(text7, first7, second7)
    assert (
        result7 == expected7
    ), f"Test Case 7 Failed: Expected {expected7}, got {result7}"
    print("Passed")

    # Test Case 8: First and second words not in text
    print("Test Case 8: First and second words not in text")
    text8 = "the quick brown fox jumps over the lazy dog"
    first8, second8 = "cat", "dog"
    expected8 = []
    result8 = solution.findOcurrences(text8, first8, second8)
    assert (
        result8 == expected8
    ), f"Test Case 8 Failed: Expected {expected8}, got {result8}"
    print("Passed")


if __name__ == "__main__":
    test_find_ocurrences()
