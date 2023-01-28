'''


'''
#36ms
class Solution(object):
    def longestCommonPrefix(self, strs):
        output=""
        for n in zip(*strs):
            if len(set(n))==1:
                output+=n[0]
            else:
                return output
            
        return output
    
    

    #3ms
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs.pop(0)

        for word in strs:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
        
        return prefix
      
      
 #best space complexity
class Solution(object):
    def longestCommonPrefix(self, strs):
        
        longestPrefix = ""

        # Use the python any operator to check if the first char of the strings in the list are the same
        # If they are, add it to the longestPrefix and continue

        # Check if the list is empty
        if not strs:
            return longestPrefix
        
        # Check if the list has only one element
        if len(strs) == 1:
            return strs[0]
        
        # Use the python any operator to check if the first char of the strings in the list are the same
        # If they are, add it to the longestPrefix and continue
        for i in range(len(strs[0])):
            if any(i == len(strs[j]) or strs[0][i] != strs[j][i] for j in range(len(strs))):
                return longestPrefix
            longestPrefix += strs[0][i]

        return longestPrefix
      
      
