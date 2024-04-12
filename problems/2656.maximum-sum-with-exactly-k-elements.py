from typing import *


# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max = nums[0]
        for i in nums:
            tmp = ((2 * i + (k - 1)) * k) // 2
            if tmp > max:
                max = tmp
        return max
