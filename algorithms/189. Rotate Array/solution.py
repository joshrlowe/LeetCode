from typing import List


#
class Solution1:
    # Self-created approach - good if I wanted to show I know how reverse could be implemented for indices
    # O(n) time complexity
    # O(1) space complexity
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse_indices(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k %= len(nums)
        nums.reverse()
        reverse_indices(0, k - 1)
        reverse_indices(k, len(nums) - 1)


class Solution2:
    # More Pythonic Approach
    # O(n) Time Complexity
    # O(1) Space Complexity - List slicing does not use extra space because of Python's efficient implementation, which avoids memory allocation
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        if k > 0:
            nums.reverse()
            nums[:k] = nums[:k][::-1]
            nums[k:] = nums[k:][::-1]
