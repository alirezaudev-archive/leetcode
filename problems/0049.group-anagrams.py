from typing import List

# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for i in strs:
            chars = ''.join(sorted(i))
            anagrams.setdefault(chars, []).append(i)

        return list(anagrams.values())

print(Solution().groupAnagrams([""]))