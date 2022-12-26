"""
Given an integer n represented as a string, return the smallest good base of n.

We call k >= 2 a good base of n, if all digits of n base k are 1's.
"""
from math import log2
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        """ O(log n) """
        n = int(n)
        max_cnt = int(log2(n))
        for cnt in range(max_cnt, 1, -1):
            base = int(n**(cnt**(-1)))
            if n - 1 == base * (n - base ** cnt):
                return str(base)

        return str(n - 1)

