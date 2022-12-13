"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
"""
def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)) :
            s[i] = [char for char in s[i]]
            s[i].reverse()
            s[i] = ("".join(s[i]))
        s  = " ".join(s)

        return s
