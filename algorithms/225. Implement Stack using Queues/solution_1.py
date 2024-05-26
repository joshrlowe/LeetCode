from collections import deque


class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0


def test_my_stack():
    # Test Case 1: Basic functionality
    print("Test Case 1: Basic functionality")
    stack1 = MyStack()
    stack1.push(1)
    stack1.push(2)
    result1_top = stack1.top()
    result1_pop = stack1.pop()
    result1_empty = stack1.empty()
    assert result1_top == 2, f"Test Case 1 Failed: Expected top 2, got {result1_top}"
    assert result1_pop == 2, f"Test Case 1 Failed: Expected pop 2, got {result1_pop}"
    assert (
        result1_empty == False
    ), f"Test Case 1 Failed: Expected empty False, got {result1_empty}"
    print("Passed")

    # Test Case 2: Single element
    print("Test Case 2: Single element")
    stack2 = MyStack()
    stack2.push(3)
    result2_top = stack2.top()
    result2_pop = stack2.pop()
    result2_empty = stack2.empty()
    assert result2_top == 3, f"Test Case 2 Failed: Expected top 3, got {result2_top}"
    assert result2_pop == 3, f"Test Case 2 Failed: Expected pop 3, got {result2_pop}"
    assert (
        result2_empty == True
    ), f"Test Case 2 Failed: Expected empty True, got {result2_empty}"
    print("Passed")

    # Test Case 3: Multiple elements
    print("Test Case 3: Multiple elements")
    stack3 = MyStack()
    for i in range(1, 6):
        stack3.push(i)
    result3_top = stack3.top()
    result3_pop = [stack3.pop() for _ in range(5)]
    result3_empty = stack3.empty()
    assert result3_top == 5, f"Test Case 3 Failed: Expected top 5, got {result3_top}"
    assert result3_pop == [
        5,
        4,
        3,
        2,
        1,
    ], f"Test Case 3 Failed: Expected pop [5, 4, 3, 2, 1], got {result3_pop}"
    assert (
        result3_empty == True
    ), f"Test Case 3 Failed: Expected empty True, got {result3_empty}"
    print("Passed")

    # Test Case 4: Empty stack
    print("Test Case 4: Empty stack")
    stack4 = MyStack()
    result4_empty = stack4.empty()
    assert (
        result4_empty == True
    ), f"Test Case 4 Failed: Expected empty True, got {result4_empty}"
    print("Passed")

    # Test Case 5: Push and pop multiple times
    print("Test Case 5: Push and pop multiple times")
    stack5 = MyStack()
    stack5.push(10)
    stack5.push(20)
    result5_top_1 = stack5.top()
    result5_pop_1 = stack5.pop()
    result5_push = stack5.push(30)
    result5_top_2 = stack5.top()
    result5_pop_2 = stack5.pop()
    result5_pop_3 = stack5.pop()
    result5_empty = stack5.empty()
    assert (
        result5_top_1 == 20
    ), f"Test Case 5 Failed: Expected top 20, got {result5_top_1}"
    assert (
        result5_pop_1 == 20
    ), f"Test Case 5 Failed: Expected pop 20, got {result5_pop_1}"
    assert (
        result5_top_2 == 30
    ), f"Test Case 5 Failed: Expected top 30, got {result5_top_2}"
    assert (
        result5_pop_2 == 30
    ), f"Test Case 5 Failed: Expected pop 30, got {result5_pop_2}"
    assert (
        result5_pop_3 == 10
    ), f"Test Case 5 Failed: Expected pop 10, got {result5_pop_3}"
    assert (
        result5_empty == True
    ), f"Test Case 5 Failed: Expected empty True, got {result5_empty}"
    print("Passed")


if __name__ == "__main__":
    test_my_stack()
