"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def closure(grid):
            m = len(grid)
            n = len(grid[0])
            dirs = ((1,0), (0,1), (-1,0), (0,-1))
            sum_pair = lambda p1, p2: (p1[0]+ p2[0], p1[1] + p2[1])
            area = 0
            visited = set()
            def bfs(r, c):
                nonlocal visited, area
                visited.add((r, c))
                area += 1
                for d in dirs:
                    cords = sum_pair(d, (r, c))
                    if 0 <= cords[0] < m and 0 <= cords[1] < n \
                        and grid[cords[0]][cords[1]] == 1 and \
                            cords not in visited:
                        bfs(cords[0], cords[1])
                return (area, visited)
            return bfs
        visited = set()
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area, visited_now = closure(grid)(r, c)
                    visited.update(visited_now)
                    max_area = max(max_area, area)

        return max_area
