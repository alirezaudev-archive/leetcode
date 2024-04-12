from typing import *


# https://leetcode.com/problems/adding-spaces-to-a-string/
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = []
        start = 0
        for end in spaces:
            arr.append(s[start:end])
            start = end
        arr.append(s[start:])
        return ' '.join(arr)
