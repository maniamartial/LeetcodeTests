'''

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


'''

class Solution(object):
    def firstUniqChar(self, s):
        
        chars = dict()
        
        for char in s:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1

        
        for i in range(0, len(s)):
            if chars[s[i]] == 1:
                return i
            
        return -1
    
        
