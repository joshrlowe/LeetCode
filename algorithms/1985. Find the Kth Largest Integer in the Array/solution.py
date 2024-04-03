# Self-Implemented Sorting
# O(nlog(n)) time complexity
# O(n) space complexity
def kthLargestNumber(nums, k) -> str:
    def merge_sort(lst):
        if len(lst) < 2:
            return lst
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        i, j = 0, 0
        new_lst = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                new_lst.append(left[i])
                i += 1
            else:
                new_lst.append(right[j])
                j += 1
        new_lst.extend(left[i:])
        new_lst.extend(right[j:])
        lst = new_lst
        return lst

    nums = [int(num) for num in nums]
    nums = merge_sort(nums)
    return str(nums[-k])


# Python Sorting - TimSort
# O(nlog(n)) Time Complexity
def kthLargestNumber(nums, k):
    nums = [int(num) for num in nums]
    nums.sort()
    return str(nums[-k])


print(kthLargestNumber(["3", "6", "7", "10"], 4))


"""
Optimal Solution:
https://chat.openai.com/share/e9d0b40e-11fc-4823-9d48-400762dc398e
"""
