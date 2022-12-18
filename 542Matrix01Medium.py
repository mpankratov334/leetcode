"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # naive bfs O(m*n*m*n)
        rows = len(mat)
        cols = len(mat[0])
        
        def bfs(r,c):
            visited = set()
            q = collections.deque()
            q.extend([(r + 1,c), (r - 1, c), (r, c - 1), (r, c + 1)])
            dist = 0
            while q:
                dist += 1
                for _ in range(len(q)):          
                    r,c = q.popleft()
                    if (r,c) not in visited and 0 <= r < rows \
                        and 0 <= c < cols:
                        if mat[r][c] == 0:
                            return dist
                        q.extend([(r + 1,c), (r - 1, c), (r, c - 1), (r, c + 1)])
                    visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    mat[r][c] = bfs(r,c)

        return mat


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Induction O(m*n)
        m, n = len(mat), len(mat[0])
        for r in range(m):
            for c in range(n):
                if mat[r][c] != 0:
                    top = mat[r - 1][c] if r > 0 else float('inf')
                    left = mat[r][c - 1] if c > 0 else float('inf')
                    mat[r][c] = min(top, left) + 1

        for r in range(m - 1, -1, -1 ):
            for c in range(n - 1, -1, -1):
                if mat[r][c] != 0:
                    bot = mat[r + 1][c] if r + 1 < m else float('inf')
                    right = mat[r][c + 1] if c + 1 < n else float('inf')
                    mat[r][c] = min(min(bot, right) + 1, mat[r][c])
        return mat
