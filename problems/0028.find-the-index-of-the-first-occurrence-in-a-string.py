# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLength = len(needle)
        for i in range(len(haystack) - needleLength + 1):
            if needle == haystack[i:i + needleLength]:
                return i
        return -1
