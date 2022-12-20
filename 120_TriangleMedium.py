"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row,
you may move to either index i or index i + 1 on the next row.
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)
        if height == 1: return triangle[0][0]

        for h in range(1, height):
            level_lenght = len(triangle[-h])

            for i in range(level_lenght - 1):

                now_number = triangle[-h - 1][i]
                left = triangle[-h][i]
                right = triangle[-h][i + 1]
                min_path = min(left, right) + now_number
                triangle[-h - 1][i] = min_path

        return triangle[0][0]
