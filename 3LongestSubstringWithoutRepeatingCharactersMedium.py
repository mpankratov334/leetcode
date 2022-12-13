"""
Given a string s, find the length of the longest 
substring without repeating characters.
"""
# version 1.0
def lengthOfLongestSubstring(self, s: str) -> int:
        word = []
        dct = {}
        max_length , cur_length = 0, 0
        i = 0
        while i < len(s):
            print(word)
            if s[i] not in dct:
                dct[s[i]] = i
                word.append(s[i])
                cur_length += 1
            else:
                max_length = max(max_length, cur_length)
                char_index = word.index(s[i])

                for el in word[:char_index]:
                    dct.pop(el)
                
                word[:char_index+1] = []
                word.append(s[i])
                cur_length = i - dct[s[i]]
                dct[s[i]] = i

            i += 1
            
        max_length = max(max_length, cur_length)
        
        return max_length
# version 2.0
def lengthOfLongestSubstring(self, s: str) -> int:
  seen = dict()
  start = 0
  m = 0
  for i, c in enumerate(s):
    if c in seen and seen[c] >= start:
        start = seen[c] + 1
    m = max(m, i - start + 1)
    seen[c] = i
    
  return m    
