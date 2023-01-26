





#my code, i decided to use the reverse 49ms
class Solution(object):
    def isPalindrome(self, s):
        slist=list(str(s.lower()))
        new_array=[]
        
        for i in slist:
            if i in "abcdefghijklmnopqrstuvwxyz1234567890":
                new_array.append(i)
                
        new_array_reverse=new_array[::-1]
        if new_array==new_array_reverse:
            return True
        else:
            return False
          
#fastest, thoough close to mine
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(c for c in s if c.isalnum()).lower()
        return s == s[::-1]
      
 #space complexity
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
          
