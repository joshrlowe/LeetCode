from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        s2_freq = {}

        l = 0
        for r in range(len(s2)):
            s2_freq[s2[r]] = s2_freq.get(s2[r], 0) + 1

            if r - l + 1 > len(s1):
                if s2_freq[s2[l]] == 1:
                    del s2_freq[s2[l]]
                else:
                    s2_freq[s2[l]] -= 1
                l += 1

            if s1_freq == s2_freq:
                return True

        return False


def test_checkInclusion():
    solution = Solution()

    # Test case 1: s1 is a permutation of the beginning of s2
    print("Test case 1: s1 is a permutation of the beginning of s2")
    s1 = "ab"
    s2 = "eidbaooo"
    expected = True
    assert solution.checkInclusion(s1, s2) == expected, f"Test case 1 failed"
    print("Passed")

    # Test case 2: s1 is not a permutation of any substring of s2
    print("Test case 2: s1 is not a permutation of any substring of s2")
    s1 = "ab"
    s2 = "eidboaoo"
    expected = False
    assert solution.checkInclusion(s1, s2) == expected, f"Test case 2 failed"
    print("Passed")

    # Test case 3: s1 is a permutation of the end of s2
    print("Test case 3: s1 is a permutation of the end of s2")
    s1 = "adc"
    s2 = "dcda"
    expected = True
    assert solution.checkInclusion(s1, s2) == expected, f"Test case 3 failed"
    print("Passed")

    # Test case 4: s1 is a permutation of a middle substring of s2
    print("Test case 4: s1 is a permutation of a middle substring of s2")
    s1 = "abc"
    s2 = "bbbca"
    expected = True
    assert solution.checkInclusion(s1, s2) == expected, f"Test case 4 failed"
    print("Passed")

    # Test case 5: s2 is empty
    print("Test case 5: s2 is empty")
    s1 = "a"
    s2 = ""
    expected = False
    assert solution.checkInclusion(s1, s2) == expected, f"Test case 5 failed"
    print("Passed")

    # Test case 6: s1 is empty
    print("Test case 6: s1 is empty")
    s1 = ""
    s2 = "a"
    expected = True
    assert solution.checkInclusion(s1, s2) == expected, f"Test case 6 failed"
    print("Passed")

    # Test case 7: s1 is longer than s2
    print("Test case 7: s1 is longer than s2")
    s1 = "abc"
    s2 = "a"
    expected = False
    assert solution.checkInclusion(s1, s2) == expected, f"Test case 7 failed"
    print("Passed")


if __name__ == "__main__":
    test_checkInclusion()
