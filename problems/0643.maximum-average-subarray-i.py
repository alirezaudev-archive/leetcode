from typing import *


# https://leetcode.com/problems/maximum-average-subarray-i/
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = sum(nums[:k])
        currSum = maxSum
        for i in range(len(nums[:-k])):
            currSum = currSum - nums[i] + nums[i + k]
            if maxSum < currSum:
                maxSum = currSum

        return maxSum / k
