# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLength = len(s)
        if sLength != len(t):
            return False

        mp = {}
        for i in range(sLength):
            mp[s[i]] = mp.get(s[i], 0) + 1
            mp[t[i]] = mp.get(t[i], 0) - 1

        return not any(value < 0 for value in mp.values())
