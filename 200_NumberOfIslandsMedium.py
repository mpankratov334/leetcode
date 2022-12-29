"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water
"""
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        cnt = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    visited.add((r,c))
                    q.append((r,c))
                    while q:
                        nowr, nowc = q.popleft()
                        if nowr + 1 < rows and \
                            grid[nowr + 1][nowc] == '1' and \
                            (nowr+ 1, nowc) not in visited: # down
                            q.append((nowr + 1, nowc))
                            visited.add((nowr + 1,nowc))
                        if nowc + 1 < cols and \
                            grid[nowr][nowc + 1] == '1' and \
                            (nowr, nowc + 1) not in visited: # right
                            q.append((nowr, nowc + 1))
                            visited.add((nowr,nowc + 1))
                        if nowr > 0 and \
                            grid[nowr - 1][nowc] == '1' and \
                            (nowr - 1, nowc) not in visited: # up
                            q.append((nowr - 1, nowc))
                            visited.add((nowr - 1, nowc))
                        if nowc > 0 and \
                            grid[nowr][nowc - 1] == '1' and \
                            (nowr, nowc - 1) not in visited: # left
                            q.append((nowr, nowc - 1))
                            visited.add((nowr, nowc - 1))
                    cnt += 1
        return cnt
