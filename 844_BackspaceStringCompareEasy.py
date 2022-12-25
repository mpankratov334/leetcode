"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""
class Solution:
    @staticmethod
    def skip_backspaces(s, s_i):
        ks = 1
        while s[s_i] != "$" and ks > 0:
            if s[s_i] != '#':
                ks -= 1
            else:
                ks += 1
            s_i -= 1
        return s_i
    def backspaceCompare(self, s: str, t: str) -> bool:
        """ time: O(n), extraspace: O(n) """
        t = "$" * (max(len(s), len(t)) - len(t) + 1) + t        
        s = "$" * (max(len(s), len(t)) - len(s) + 1) + s        
        
        s_i, t_i = len(s) - 1, len(t) - 1
        while s_i >= 0 and t_i >= 0:
            while s[s_i] == '#':
                s_i = Solution.skip_backspaces(s, s_i - 1)
            while t[t_i] =='#':
                t_i = Solution.skip_backspaces(t, t_i - 1)
            if s_i >= 0 and t_i >=0 and s[s_i] != t[t_i]:
                print(s_i, t_i)
                return False
            s_i -= 1
            t_i -= 1
        return True
