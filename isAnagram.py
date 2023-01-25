'''

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

'''
#my solution takes 85ms
class Solution(object):
    def isAnagram(self, s, t):
               
        ssort=sorted(s)
        tsort=sorted(t)
        
        if ssort==tsort:
            return True
        return False
    
    
    #Best time complexity 16ms
    
    from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
       
        # map = Counter(s)
        # for letter in t:
        #     map[letter] -= 1
        #     if map[letter]==0: del map[letter]
        # return len(map)==0

        return all(s.count(x) == t.count(x) for x in "abcdefghijklmnopqrstuvwxyz")
    
    
    
    #Best space complexity
    
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        sMap, tMap = {}, {}
        for ch in s:
            if ch in sMap.keys():
                sMap[ch] += 1
            else:
                sMap[ch] = 1
        
        for ch in t:
            if ch in tMap.keys():
                tMap[ch] += 1
            else:
                tMap[ch] = 1
        
        for ch in sMap.keys():
            sCount = sMap.get(ch, 0)
            tCount = tMap.get(ch, 0)
            if sCount != tCount:
                return False
        return True
   


        
