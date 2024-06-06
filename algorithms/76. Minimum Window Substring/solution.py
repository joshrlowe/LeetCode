class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""


def run_test_case(test_case_num, s, t, expected):
    solution = Solution()
    result = solution.minWindow(s, t)
    assert (
        result == expected
    ), f"Test case {test_case_num} failed: expected '{expected}', got '{result}'"
    print(f"Test case {test_case_num} - Passed")


def test_minWindow():
    # Test case 1: Substring at the beginning
    print("Test case 1: Substring at the beginning")
    run_test_case(1, "ADOBECODEBANC", "ABC", "BANC")

    # Test case 2: No valid substring
    print("Test case 2: No valid substring")
    run_test_case(2, "ADOBECODEBANC", "XYZ", "")

    # Test case 3: Substring is the entire string
    print("Test case 3: Substring is the entire string")
    run_test_case(3, "A", "A", "A")

    # Test case 4: Substring is the last part
    print("Test case 4: Substring is the last part")
    run_test_case(4, "ADOBECODEBANC", "CBA", "BANC")

    # Test case 5: Substring with repeated characters
    print("Test case 5: Substring with repeated characters")
    run_test_case(5, "AAABBBCCC", "ABC", "ABBBC")

    # Test case 6: Empty string `t`
    print("Test case 6: Empty string `t`")
    run_test_case(6, "A", "", "")

    # Test case 7: Multiple potential windows
    print("Test case 7: Multiple potential windows")
    run_test_case(7, "aaflslflsldkalskaaa", "aaa", "aaa")

    # Test case 8: `s` and `t` are the same
    print("Test case 8: `s` and `t` are the same")
    run_test_case(8, "ABC", "ABC", "ABC")

    # Test case 9: t is longer than s
    print("Test case 9: t is longer than s")
    run_test_case(9, "AB", "ABC", "")


if __name__ == "__main__":
    test_minWindow()
