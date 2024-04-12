from typing import List


# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        commonPrefix = strs[0]
        for i in range(1, len(strs)):
            commonPrefix = self.findPrefix(commonPrefix, strs[i])
            if commonPrefix == '':
                return ''

        return commonPrefix

    def findPrefix(self, w1: str, w2: str) -> str:
        (shortest, longest,) = sorted([w1, w2], key=len)
        prefix = ''
        i = 0
        while i < len(shortest) and shortest[i] == longest[i]:
            prefix += shortest[i]
            i += 1
        return prefix
