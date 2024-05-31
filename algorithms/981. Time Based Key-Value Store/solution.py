class TimeMap:

    def __init__(self):
        self.keyTimeTable = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyTimeTable:
            self.keyTimeTable[key] = []
        self.keyTimeTable[key].append(tuple([timestamp, value]))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyTimeTable or timestamp < self.keyTimeTable[key][0][0]:
            return ""

        l, r = 0, len(self.keyTimeTable[key]) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamp > self.keyTimeTable[key][m][0]:
                l = m + 1
            elif timestamp < self.keyTimeTable[key][m][0]:
                r = m - 1
            else:
                return self.keyTimeTable[key][m][1]

        return self.keyTimeTable[key][r][1]


def test_time_map():
    time_map = TimeMap()

    # Test Case 1: Basic set and get
    print("Test 1: Basic set and get")
    time_map.set("foo", "bar", 1)
    assert time_map.get("foo", 1) == "bar", "Test 1 Failed"
    print("Test 1 Passed")

    # Test Case 2: Get with a timestamp before any set timestamp
    print("Test 2: Get with a timestamp before any set timestamp")
    assert time_map.get("foo", 0) == "", "Test 2 Failed"
    print("Test 2 Passed")

    # Test Case 3: Get with a timestamp after set timestamp
    print("Test 3: Get with a timestamp after set timestamp")
    time_map.set("foo", "bar2", 4)
    assert time_map.get("foo", 5) == "bar2", "Test 3 Failed"
    print("Test 3 Passed")

    # Test Case 4: Multiple sets with same key
    print("Test 4: Multiple sets with same key")
    time_map.set("foo", "bar3", 7)
    time_map.set("foo", "bar4", 10)
    assert time_map.get("foo", 6) == "bar2", "Test 4 Failed"
    assert time_map.get("foo", 8) == "bar3", "Test 4 Failed"
    assert time_map.get("foo", 10) == "bar4", "Test 4 Failed"
    print("Test 4 Passed")

    # Test Case 5: Multiple keys
    print("Test 5: Multiple keys")
    time_map.set("baz", "qux", 3)
    assert time_map.get("baz", 3) == "qux", "Test 5 Failed"
    assert time_map.get("baz", 4) == "qux", "Test 5 Failed"
    print("Test 5 Passed")

    # Test Case 6: Large timestamps and multiple keys
    print("Test 6: Large timestamps and multiple keys")
    time_map.set("alpha", "value1", 1000000)
    time_map.set("alpha", "value2", 2000000)
    assert time_map.get("alpha", 1500000) == "value1", "Test 6 Failed"
    assert time_map.get("alpha", 2500000) == "value2", "Test 6 Failed"
    print("Test 6 Passed")

    # Test Case 7: Edge case with maximum length of key and value
    print("Test 7: Edge case with maximum length of key and value")
    long_key = "k" * 100
    long_value = "v" * 100
    time_map.set(long_key, long_value, 1234567)
    assert time_map.get(long_key, 1234567) == long_value, "Test 7 Failed"
    assert time_map.get(long_key, 2000000) == long_value, "Test 7 Failed"
    print("Test 7 Passed")

    # Test Case 8: Get with no corresponding set timestamp
    print("Test 8: Get with no corresponding set timestamp")
    assert time_map.get("foo", 11) == "bar4", "Test 8 Failed"
    assert time_map.get("foo", 2) == "bar", "Test 8 Failed"
    print("Test 8 Passed")


if __name__ == "__main__":
    test_time_map()
