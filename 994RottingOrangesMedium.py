"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""
# O ( n * m * max(n,m) )
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:            
        ans = 0
        rows = len(grid)
        columns = len(grid[0])

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    grid[r][c] = (2, 0) 
                elif grid[r][c] == 1:
                    grid[r][c] = (1, float("inf"))
                else:
                    grid[r][c] = (0, float("inf"))
       
        for i in range(max(max(rows, columns)//3, 2)):
            for r in range(rows):
                for c in range(columns):
                    if grid[r][c][0] == 1:
                        left = grid[r][c - 1][1] if c > 0 else float("inf")
                        top = grid[r-1][c][1] if r > 0 else float("inf")
                        grid[r][c] = (1, min(min(left, top) + 1, grid[r][c][1]) )

            for r in range(rows - 1, -1 , -1):
                for c in range(columns - 1, -1 , -1):
                    if grid[r][c][0] == 1:
                        right = grid[r][c + 1][1] if c + 1 < columns else float("inf")
                        top = grid[r+1][c][1] if r  + 1  < rows  else float("inf")
                        dist = min(min(top, right) + 1, grid[r][c][1])
                        grid[r][c] = (1, dist)

        for r in range(rows):
            for c in range(columns):
                if grid[r][c][0] == 1:
                    ans = max(ans, grid[r][c][1])

        return -1 if ans == float("inf") else ans
      
# with queue (deque) O(n * m)     
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:            
        ans = 0
        rows = len(grid)
        columns = len(grid[0])
        q = collections.deque()
        visited = set()
        
        if all(all(x == 0 for x in grid[r]) for r in range(rows)):
            return ans

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
        while q:
            ans += 1 
            turns = len(q)
            for i in range(turns):
                r,c = q.popleft()
                if r + 1 < rows and (r + 1, c) not in visited\
                    and grid[r + 1][c] == 1:
                    grid[r+1][c] = 2
                    q.append((r + 1, c))
                    visited.add((r + 1, c))

                if r > 0 and (r - 1, c) not in visited\
                    and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    q.append((r - 1, c))
                    visited.add((r - 1, c))
                
                if c > 0 and (r, c - 1) not in visited\
                    and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    q.append((r, c - 1))
                    visited.add((r, c - 1))

                if c + 1 < columns and (r, c + 1) not in visited\
                    and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    q.append((r, c + 1))
                    visited.add((r, c + 1))

        if any(any( x == 1 for x in grid[r]) for r in range(rows)):
            return -1

        return ans - 1      
