'''

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

#Dint even try this, but i understood the solutiion, solution run in 17ms
class Solution(object):
    def strStr(self, haystack, needle):
        nl, ml = len(needle), len(haystack)
        if nl == 0:
            return nl
        if ml < nl:
            return -1
        for i in range(ml - nl + 1):
            if haystack[i:i+nl] == needle:
                return i
        return -1
      
   #time complexity run in 3ms
  class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
                
        return -1
      
   #space complexity
  class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        start_index = len(needle)
        for index in range(start_index,len(haystack)+1):
            if(needle==haystack[index-len(needle):index]):
                return index-len(needle)
        return -1
        
                
                
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        
            
