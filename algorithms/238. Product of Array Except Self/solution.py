from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Each number is equal to the product of all terms to the left times the product of all terms to the right
        So, if we multiply from the left then multiply from the right, then we would get the product of array 
        except self in O(2n) \in O(n) time.
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        res = [1] * len(nums)
        left, right = 1, 1
        for i in range(len(nums)):
            res[i] *= left
            left *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res