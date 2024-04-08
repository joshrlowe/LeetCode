from typing import List

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        def find_sub_intersection(a1, a2):
            i, j = 0, 0
            result = []
            while i < len(a1) and j < len(a2):
                if a1[i] < a2[j]:
                    i += 1
                elif a1[i] > a2[j]:
                    j += 1
                else:
                    result.append(a1[i])
                    i += 1
                    j += 1
            return result

        arr1_arr2 = find_sub_intersection(arr1, arr2)
        return find_sub_intersection(arr1_arr2, arr3)