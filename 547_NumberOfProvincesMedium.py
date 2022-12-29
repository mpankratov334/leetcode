"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected 
directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and 
isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""
from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """ O(n) """
        n = len(isConnected)
        ans = 0
        graph = {i + 1: set() for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    graph[i + 1].add(j + 1)
                    graph[j + 1].add(i + 1)

        visited = set()
        q = deque()
        for el in graph:
            if el in visited: continue
            ans += 1
            q.append(el)
            visited.add(el)
            while q:
                now_el = q.popleft()
                for nxt in graph[now_el]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
        return ans
