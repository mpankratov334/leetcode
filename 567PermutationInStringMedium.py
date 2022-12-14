"""
"""
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
