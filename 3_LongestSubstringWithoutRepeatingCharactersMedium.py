"""
Given a string s, find the length of the longest 
substring s without repeating characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      """ O(n) """
        ans = 0
        left = 0
        d = dict()
        for right, c in enumerate(s):
            if c in d and d[c] >= left:
                left = d[c] + 1
            d[c] = right
            now = right - left + 1
            ans = max(ans, now)
        
        return ans
