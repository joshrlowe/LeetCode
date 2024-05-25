class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


def test_min_stack():
    # Test Case 1: Basic functionality
    print("Test Case 1: Basic functionality")
    minStack1 = MinStack()
    minStack1.push(-2)
    minStack1.push(0)
    minStack1.push(-3)
    assert (
        minStack1.getMin() == -3
    ), f"Test Case 1 Failed: Expected -3, got {minStack1.getMin()}"
    minStack1.pop()
    assert (
        minStack1.top() == 0
    ), f"Test Case 1 Failed: Expected 0, got {minStack1.top()}"
    assert (
        minStack1.getMin() == -2
    ), f"Test Case 1 Failed: Expected -2, got {minStack1.getMin()}"
    print("Passed")

    # Test Case 2: Push and pop operations
    print("Test Case 2: Push and pop operations")
    minStack2 = MinStack()
    minStack2.push(1)
    minStack2.push(2)
    minStack2.push(-1)
    minStack2.push(3)
    assert (
        minStack2.getMin() == -1
    ), f"Test Case 2 Failed: Expected -1, got {minStack2.getMin()}"
    minStack2.pop()
    assert (
        minStack2.getMin() == -1
    ), f"Test Case 2 Failed: Expected -1, got {minStack2.getMin()}"
    minStack2.pop()
    assert (
        minStack2.getMin() == 1
    ), f"Test Case 2 Failed: Expected 1, got {minStack2.getMin()}"
    print("Passed")

    # Test Case 3: Push and pop all elements
    print("Test Case 3: Push and pop all elements")
    minStack3 = MinStack()
    minStack3.push(5)
    minStack3.push(3)
    minStack3.push(7)
    assert (
        minStack3.getMin() == 3
    ), f"Test Case 3 Failed: Expected 3, got {minStack3.getMin()}"
    minStack3.pop()
    minStack3.pop()
    minStack3.pop()
    try:
        minStack3.getMin()
        assert False, "Test Case 3 Failed: Expected an error, got None"
    except IndexError:
        print("Passed")

    # Test Case 4: Negative numbers
    print("Test Case 4: Negative numbers")
    minStack4 = MinStack()
    minStack4.push(-1)
    minStack4.push(-5)
    minStack4.push(-3)
    assert (
        minStack4.getMin() == -5
    ), f"Test Case 4 Failed: Expected -5, got {minStack4.getMin()}"
    minStack4.pop()
    assert (
        minStack4.getMin() == -5
    ), f"Test Case 4 Failed: Expected -5, got {minStack4.getMin()}"
    minStack4.pop()
    assert (
        minStack4.getMin() == -1
    ), f"Test Case 4 Failed: Expected -1, got {minStack4.getMin()}"
    print("Passed")

    # Test Case 5: Single element stack
    print("Test Case 5: Single element stack")
    minStack5 = MinStack()
    minStack5.push(2)
    assert (
        minStack5.getMin() == 2
    ), f"Test Case 5 Failed: Expected 2, got {minStack5.getMin()}"
    assert (
        minStack5.top() == 2
    ), f"Test Case 5 Failed: Expected 2, got {minStack5.top()}"
    minStack5.pop()
    try:
        minStack5.top()
        assert False, "Test Case 5 Failed: Expected an error, got None"
    except IndexError:
        print("Passed")

    # Test Case 6: Duplicates
    print("Test Case 6: Duplicates")
    minStack6 = MinStack()
    minStack6.push(1)
    minStack6.push(2)
    minStack6.push(2)
    minStack6.push(1)
    assert (
        minStack6.getMin() == 1
    ), f"Test Case 6 Failed: Expected 1, got {minStack6.getMin()}"
    minStack6.pop()
    assert (
        minStack6.getMin() == 1
    ), f"Test Case 6 Failed: Expected 1, got {minStack6.getMin()}"
    minStack6.pop()
    assert (
        minStack6.getMin() == 1
    ), f"Test Case 6 Failed: Expected 1, got {minStack6.getMin()}"
    minStack6.pop()
    assert (
        minStack6.getMin() == 1
    ), f"Test Case 6 Failed: Expected 1, got {minStack6.getMin()}"
    minStack6.pop()
    try:
        minStack6.getMin()
        assert False, "Test Case 6 Failed: Expected an error, got None"
    except IndexError:
        print("Passed")


if __name__ == "__main__":
    test_min_stack()
