
'''

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


'''




#best solution whih took less time 
'''class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c not in magazine:
                return False
            magazine = magazine.replace(c, "", 1)
        return True'''

#my solution : took 36 ms
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        magazineDict = {}

        for s in magazine:
            magazineDict[s] = magazineDict[s] + 1 if s in magazineDict else 1

        for s in ransomNote:
            if s in magazineDict and magazineDict[s] > 0:
                magazineDict[s] -= 1
            else:
                return False
        
        return True
      
      #Space and time complexity
      '''
      The time complexity is O(n^2) because for each character in the ransom note, the replace method is used to remove it from the magazine. This method has a time complexity of O(n) because it needs to iterate through the entire magazine to find the first instance of the character. Since the loop is iterating n times over the ransom note, the time complexity is O(n) * O(n) = O(n^2).

The space complexity is O(1) because the function only uses a constant amount of extra memory to store the loop variables and the boolean result. The magazine string itself is passed as an argument to the function, so the function does not need to create a copy of the magazine to work with.

Note: The time complexity can be decreased to O(n) by using a hash table (dictionary or hashmap) or counting array, or some similar data structure which can look up the occurrences of the character in constant time. In that case, space complexity would be O(n)
     
      '''
      
      
