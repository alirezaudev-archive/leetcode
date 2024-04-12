from typing import List

# https://leetcode.com/problems/concatenation-of-array/description/
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = nums[:]
        for i in nums:
            result.append(i)
        return result # or `nums * 2`

