"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        memory = { i: None for i in range(1, n + 1)}
        memory[1] = 1
        memory[2] = 2
        def fibonachy(n):
            nonlocal memory
            if memory[n]:
                return memory[n]
            s = fibonachy(n - 2) + fibonachy(n - 1)
            memory[n] = s
            return s

        return fibonachy(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        one_back, two_back = 1, 0
        for _ in range(n-1):
            one_back, two_back = one_back + two_back, one_back
        return one_back + two_back
