# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ti, si = 0

        tLength = len(t)
        sLength = len(s)

        while sLength > si and tLength > ti:
            if s[si] == t[ti]:
                si += 1
            ti += 1

        return sLength == si
