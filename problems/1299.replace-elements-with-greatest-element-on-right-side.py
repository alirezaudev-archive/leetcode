from typing import List


# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = -1
        i = len(arr) - 1
        while i >= 0:
            temp = arr[i]
            arr[i] = m
            if temp > m:
                m = temp
            i -= 1
        return arr
