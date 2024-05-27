from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.extend([str(len(s)), "#", s])
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res


def test_codec():
    codec = Codec()

    # Test Case 1: Basic encoding and decoding
    print("Test 1: Basic encoding and decoding")
    strs = ["hello", "world"]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    assert decoded == strs, f"Test 1 Failed: expected {strs}, got {decoded}"
    print("Test 1 Passed")

    # Test Case 2: Empty strings
    print("Test 2: Empty strings")
    strs = ["", ""]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    assert decoded == strs, f"Test 2 Failed: expected {strs}, got {decoded}"
    print("Test 2 Passed")

    # Test Case 3: Strings with spaces
    print("Test 3: Strings with spaces")
    strs = ["hello world", " "]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    assert decoded == strs, f"Test 3 Failed: expected {strs}, got {decoded}"
    print("Test 3 Passed")

    # Test Case 4: Single character strings
    print("Test 4: Single character strings")
    strs = ["a", "b", "c"]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    assert decoded == strs, f"Test 4 Failed: expected {strs}, got {decoded}"
    print("Test 4 Passed")

    # Test Case 5: Mixed length strings
    print("Test 5: Mixed length strings")
    strs = ["short", "medium length", "a very very long string"]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    assert decoded == strs, f"Test 5 Failed: expected {strs}, got {decoded}"
    print("Test 5 Passed")

    # Test Case 6: Special characters
    print("Test 6: Special characters")
    strs = ["!@#", "$%^", "&*()"]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    assert decoded == strs, f"Test 6 Failed: expected {strs}, got {decoded}"
    print("Test 6 Passed")

    # Test Case 7: Long strings
    print("Test 7: Long strings")
    strs = ["a" * 1000, "b" * 2000]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    assert decoded == strs, f"Test 7 Failed: expected {strs}, got {decoded}"
    print("Test 7 Passed")

    # Test Case 8: Empty list
    print("Test 8: Empty list")
    strs = []
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    assert decoded == strs, f"Test 8 Failed: expected {strs}, got {decoded}"
    print("Test 8 Passed")


if __name__ == "__main__":
    test_codec()
