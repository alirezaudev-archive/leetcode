# https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0
        startCount = False
        i = len(s) - 1
        while 0 <= i:
            char = s[i]
            if (not startCount) and char != ' ':
                startCount = True

            if startCount:
                if char == ' ':
                    break
                c += 1

            i -= 1

        return c


print(Solution().lengthOfLastWord("hello world   "))
