"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """ O(n) """
        if len(p) > len(s): return []
        ans = []
        dict_p = dict()
        for letter in p:
            dict_p[letter] = dict_p.get(letter, 0) + 1

        same = 0
        now_dict = dict()
        for letter in s[:len(p)]:
            if letter in dict_p:
                now_dict[letter] = now_dict.get(letter, 0) + 1
                if now_dict[letter] == dict_p[letter]: same += 1
                elif now_dict[letter] == dict_p[letter] + 1: same -= 1
        if same == len(dict_p):
            ans.append(0) 

        right = len(p) - 1
        for left in range(len(s) - len(p)):
            right += 1
            lc = s[left]
            rc = s[right]
            if lc in now_dict:
                if now_dict[lc] == dict_p[lc]: same -= 1
                if now_dict[lc] == dict_p[lc] + 1: same += 1 
                now_dict[lc] -= 1
                if now_dict[lc] == 0: now_dict.pop(lc)
            if rc in dict_p: 
                now_dict[rc] = now_dict.get(rc, 0) + 1
                if now_dict[rc] == dict_p[rc]: same += 1
                if now_dict[rc] == (dict_p[rc] + 1): same -= 1
            if same == len(dict_p): ans.append(left+1) 
        return ans
