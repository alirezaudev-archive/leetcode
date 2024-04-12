# https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/description/
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        beautiful = 0

        i = low+1
        while i <= high:
            if i == 10:
                beautiful += 1
                continue

            iStr = str(i)
            if len(iStr) % 2 != 0:
                i = 10 ** (len(iStr))

            if i % k == 0 and self.isBeautiful(i):
                beautiful += 1

            i += 1

        return beautiful

    def isBeautiful(self, i) -> bool:
        evens = 0
        strI = str(i)
        for digit in strI:
            if int(digit) % 2 == 0:
                evens += 1

        return (len(strI) - evens) == evens

low = 1
high = 10
k = 1
print(Solution().numberOfBeautifulIntegers(low, high, k))

