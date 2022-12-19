"""
You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.

"""
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # O(n*m) 
        rows = len(grid)
        cols = len(grid[0])
        ans = [[0 for c in range(cols)] for r in range(rows)]

        def counter(type, i):
            if type[:-3] == "zeros":
                t = 0
            else:
                t = 1
            if type[-3:] == "Row":
                return grid[i].count(t)

            if type[-3:] == "Col":
                for r in range(rows):
                    if grid[r][i] == t:
                        count += 1
                return count

        onesRow = counter("onesRow", 0)
        zerosRow = counter("zerosRow", 0)
        ro = onesRow - zerosRow
        
        for c in range(cols):
            onesCol = counter("onesCol", c)
            zerosCol = counter("zerosCol", c)
            co = onesCol - zerosCol
            ans[0][c] = (ro, co)

        for r in range(1,rows):
            onesRow = counter("onesRow", r)
            zerosRow = counter("zerosRow",r)
            ro = onesRow - zerosRow
            for c in range(cols):
                co = ans[r - 1][c][1]
                ans[r][c] = (ro, co)

        ans = [ [ ans[r][c][0] + ans[r][c][1] for c in range(cols) ] 
                for r in range(rows)]
        return ans
