from typing import List


# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(1, numRows + 1):
            row = [1] * i
            for j in range(1, i // 2 + i % 2):
                value = triangle[-1][j - 1] + triangle[-1][j]
                row[j] = value
                row[(j + 1) * - 1] = value

            triangle.append(row)

        return triangle
