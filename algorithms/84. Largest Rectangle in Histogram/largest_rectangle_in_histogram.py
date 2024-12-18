from typing import List



def largestRectangleArea(heights: List[int]) -> int:
    maxArea = 0
    stack = []

    for i, h in enumerate(heights):
        start = i
        while stack and h < stack[-1][1]:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    return maxArea


