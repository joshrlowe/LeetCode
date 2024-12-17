from typing import List


def trap(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    maxLeft, maxRight = height[l], height[r]
    result = 0

    while l < r:
        if maxLeft < maxRight:
            l += 1
            maxLeft = max(height[l], maxLeft)
            result += maxLeft - height[l]
        else:
            r -= 1
            maxRight = max(height[r], maxRight)
            result += maxRight - height[r]

    return result
