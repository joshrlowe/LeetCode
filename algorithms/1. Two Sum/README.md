# Two Sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers in `nums` such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Solution 1: Brute Force

The brute-force approach solves the problem by checking every possible pair of elements in the array. Specifically, for each element `nums[i]`, we search the remainder of the array to find another element `nums[j]` such that their sum equals the `target`. If a valid pair is found, we return their indices.

```python
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
    return []
```

In the worst case, the above solution will search through every possible pair of elements in the array. All operations on the inner `for` loop are constant. On the first iteration, the inner loop runs $n-1$ times. On the second iteration, the inner for loop runs $n-2$ times. This pattern continues until the second to last element, where the inner for loop runs once.

The function that represents the running time with respect to input size $n$ for this algortihm is:

$T(n) = c[(n-1) + (n-2) + \ldots + 2 + 1]$

---

$[(n-1) + (n-2) + \ldots + 2 + 1]$ is an arithmetic series that can be simplified as follows:

$s = (n-1) + (n-2) + \ldots + 2 + 1$

$s = 1 + 2 + \ldots + (n-2) + (n-1)$

$2s = ((n - 1) + 1) + ((n - 2) + 2) + \ldots + (2 + (n - 2)) + (1 + (n-1)) = n\cdot(n-1)$

$s = \frac{n(n-1)}{2}$

$\therefore$ $T(n)=\frac{cn(n-1)}{2}$

---

From here, it's evident that $T(n)$ is quadratic, meaning this brute-force algorithm runs in $O(n^2)$ time.

Despite the time complexity being quadratic, the space required for this algorithm doesn't depend on the size of the input array, so only constant space is used, i.e., the space complexity for this algorithm is $O(1)$.

## Solution 2: Sorting with Two Pointers

The brute-force solution runs in quadratic time, which isn’t optimal. Let’s try to improve the time complexity.

If the input array is sorted in non-decreasing order, we can use two pointers: one pointer $i$ starting at the beginning of the array and another pointer $j$ starting at the end. This approach works because:

- Values to the right of $i$ are greater than or equal to the value at $i$,
- Values to the left of $j$ are less than or equal to the value at $j$.

Using this information, for the sum of values `nums[i] + nums[j]`, we take three possible actions:

1. If the sum is greater than the target, `nums[i] + nums[j]` is too large, so we move $j$ one step to the left (decrement $j$) to reduce the sum.
2. If the sum is less than the target, `nums[i] + nums[j]` is too small, so we move $i$ one step to the right (increment $i$) to increase the sum.
3. If the sum equals the target, return the indices $i$ and $j$, as we have found the required pair.

If $i$ and $j$ cross at any point (i.e., $i \geq j$), it means no two numbers add up to the target, and we return an empty array.

```python
def twoSum(nums: List[int], target: int) -> List[int]:
    nums.sort()
    i, j = 0, len(nums) - 1
    while i < j:
        curSum = nums[i] + nums[j]
        if curSum < target:
            i += 1
        elif curSum > target:
            j -= 1
        else:
            return [i, j]
    return []
```

The two pointers traverse the array linearly. In the worst case, the $i$ pointer is incremented $k$ times, the $j$ pointer is decremented $n - k - 1$ times, and there are $n - 2$ comparisons. This results in an $O(n)$ operation for finding the two sum. However, this is not the dominant operation in the algorithm.

Pre-sorting is the dominant operation in this algorithm. The `sort` method in Python uses **TimSort**, a hybrid algorithm that combines merge sort and insertion sort. The worst-case time complexity of TimSort is $O(n \log n)$, where $n$ is the size of the array, and the best-case runtime of TimSort is $O(n)$. This is because TimSort combines the stability and linearthmic runtime of merge sort with the efficiency of insertion sort on smaller inputs.

In summary, the time complexity for this algorithm is $O(n\log(n))$.

Presorting with TimSort requires $O(n)$ auxiliary space because TimSort uses merge sort under the hood, which has a space complexity of $O(n)$ in the worst case. No additional data structures are used in the two pointers step, which operates in constant space $O(1)$. Thus, the space complexity for this algorithm is $O(n)$.

In summary, this solution improves on the brute-force approach by reducing the time complexity from $O(n^2)$ to $O(n \log n)$ through sorting and using the two-pointers technique.

## Solution 3: One-Pass with an Auxiliary Hash Table

The brute-force and two-pointer solutions are suboptimal in terms of time complexity. To achieve a more efficient approach, we can use a hash map to store elements we’ve already encountered, along with their indices. By doing this, we can check in constant time whether the complement of the current element has already been seen.

For each number `nums[i]`, the complement needed to reach the target is `target - nums[i]`.Using a hash map, we check if the complement is already in the hash map, i.e., if we've already encountered the complement. If so, return the current index $i$ and the stored index of the complement. Otherwise, store the current number and its index in the hash map for future lookups.

This approach ensures that we process each number once and each lookup and insertion in the hash map takes amortized $O(1)$ time.

```python
def twoSum(nums: List[int], target: int) -> List[int]:
    hashMap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashMap:
            return [i, hashMap[complement]]
        hashMap[nums[i]] = i
    return []
```

The algorithm processes each element in the array exactly once, performing a constant-time lookup and insertion into the hash map for each element. Thus, the time complexity is $O(n)$, where $n$ is the size of the array.

In the worst case, all $n$ elements in `nums` are unique, and we must store each of them in the hash map. Therefore, the space complexity is $O(n)$.

This solution trades space for speed. The hash map ensures $O(1)$ lookups and insertions, significantly improving performance over searching or sorting approaches. Time is often more valuable than space in algorithm design. While space can be increased, time cannot be recovered.

This is the optimal solution to the problem, achieving linear time complexity with a single pass through the array and constant-time lookups using a hash map.
