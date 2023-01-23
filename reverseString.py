'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution(object):
    def reverseString(self, s):
        # reverse a string
        new_array=[]
        newt=[]
        '''for k in range(len(s)-1, -1, -1):
            new_array.append(s[k])
            
        return new_array
    '''
        return s.reverse()
      
      
#This was my solution, but i dont know why it fails
class Solution(object):
    def reverseString(self, s):
        # reverse a string
        new_array=[]
        newt=[]
        for k in range(len(s)-1, -1, -1):
            new_array.append(s[k])
            
        return new_array
   
 #Best time 125 s
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s[:]=s[::-1]
        
        
 #Best case for space complexity
class Solution(object):
    def reverseString(self, s):
        right=len(s)-1
        mid=len(s)//2
        
        for i in range(0,mid,1):
            s[i],s[right]=s[right],s[i]
            right-=1
        return s
