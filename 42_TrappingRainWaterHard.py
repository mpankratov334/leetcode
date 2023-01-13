"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""
class Solution:
    def trap(self, h: List[int]) -> int:
        """ time: O(n), extraspace: O(1) """
        p = h.index(max(h))
        ans = 0
        cur_m = h[0]
        for i in range(p):
            el = h[i]
            if el <= cur_m:
                ans += cur_m - el
            else:
                cur_m = el
        cur_m = h[len(h) - 1]
        for i in range(len(h) - 1, p, -1):
            el = h[i]
            if el <= cur_m:
                ans += cur_m - el
            else:
                cur_m = el
        return ans
