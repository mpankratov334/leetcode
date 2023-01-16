"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """ O(len(s2)) """
        ls1, ls2 = len(s1), len(s2)
        left, right = 0, ls1
        s1_dct = dict()
        for c in s1:
            s1_dct[c] = s1_dct.get(c, 0) + 1
        equality = 0
        intersection = dict()
        for c in s2[:ls1]:
            if c in s1_dct:
                intersection[c] = intersection.get(c, 0) + 1
                if intersection[c] <= s1_dct[c]:
                    equality += 1
        if equality == ls1: return True
        while right < ls2:
            cr = s2[right]
            cl = s2[left]
            if cl in intersection:
                if intersection[cl] <= s1_dct[cl]:
                    equality -= 1
                intersection[cl] -= 1
            if cr in s1_dct:
                intersection[cr] = intersection.get(cr, 0) + 1
                if intersection[cr] <= s1_dct[cr]:
                    equality += 1
            if equality == ls1: return True
            left += 1
            right += 1
        return False


 def checkInclusion(self, s1: str, s2: str) -> bool:
        # O((n - m) * m + n)
        l1 , l2 = len(s1), len(s2)
        
        if l1 > l2:
            return False
        
        dct_s1 = dict()
        for c in s1:
            dct_s1[c] = dct_s1.get(c,0) + 1
        dct_now = dict()
        for c in s2[:l1]:
            dct_now[c] = dct_now.get(c,0) + 1
        if dct_now == dct_s1:
            return True
        
        for i in range(l2  - l1):
            dct_now[s2[i]] -= 1
            if dct_now[s2[i]] == 0:
                dct_now.pop(s2[i])
            dct_now[s2[i + l1]] = dct_now.get(s2[i + l1],0) + 1
            if dct_now == dct_s1:
                return True
        return False
