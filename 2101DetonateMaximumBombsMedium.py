"""
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. 
This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. 
xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range.
These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.
"""
from collections import deque
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
      """ O(n * n) """
        N = len(bombs)
        graph = {i : set() for i in range(N)}
        is_detonate = lambda i1, i2: (bombs[i1][0] - bombs[i2][0])**2 + \
                (bombs[i1][1] - bombs[i2][1])**2 <= bombs[i1][2] ** 2
        for bomb in graph:
            for i in range(N):
                if is_detonate(bomb, i):
                    graph[bomb].add(i)
            graph[bomb].remove(bomb)
        m = 1
        for bomb in graph:
            q = deque()
            visited = {bomb}
            q.append(bomb)
            cnt = 0
            while q:
                cnt += 1
                now_bomb = q.popleft()
                for next_bomb in graph[now_bomb]:
                    if next_bomb not in visited:
                        q.append(next_bomb)  
                        visited.add(next_bomb)              
            m = max(cnt, m)
        return m
