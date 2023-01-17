"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
      """ O(n + m) """
        l = 0
        r = 0
        t_dict = dict()
        ls = len(s)
        m = (float('inf'), l, r)
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1
        diff = t_dict.copy()
        surpluses = dict()
        while l < ls and r < ls:
            while diff and r < ls:
                c = s[r]
                if c in t_dict and c in diff and diff[c] <= t_dict[c]:
                    diff[c] -= 1
                    if diff[c] == 0: diff.pop(c)
                elif c in t_dict:
                    surpluses[c] = surpluses.get(c, 0) + 1
                r += 1
            while not diff and l < ls:
                if m[0] > r - l + 1: m = (r - l + 1, l, r)
                c = s[l]
                if c in t_dict and c not in surpluses:
                    diff[c] = 1
                elif c in t_dict:
                    surpluses[c] -= 1
                    if surpluses[c] == 0: surpluses.pop(c)
                l += 1
        return "" if m[0] == float('inf') else s[m[1]:m[2]]
