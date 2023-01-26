'''

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
'''
#13ms
class Solution:
    def myAtoi(self, s):
        #32 bit signed integer,
        INT_MIN=-(2**31)
        INT_MAX=(2**31)-1
        
        # First, remove white space
        s=s.strip()
        
        #Second,
        first=None
        for character in s:
            if not first:
                if character.isdigit() or character in ['-','+']: 
                    first=character # Number or '-' or '+'
                else: # no valid first character(not digit,not sign)
                    break
            else: 
                if character.isdigit():
                    first+=character
                else: # not digit
                    break
        
        if not first or first in ['-','+']:
            first=0
        elif int(first)<INT_MIN:
            first=INT_MIN
        elif int(first)>INT_MAX:
            first=INT_MAX
            
        return int(first)
      
      
      
  #best time 3ms
  class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cursor = 0
        s_digits = []
        negative_bool = False
        digits_and_signs = "+-0123456789"
        digits = "0123456789"
        while cursor < n and s[cursor] not in digits_and_signs:
            if(s[cursor]!=" "):
                return 0
            cursor += 1
        if cursor == n:
            return 0
        if s[cursor] in "+-":
            negative_bool = s[cursor] == "-"
            cursor += 1
        while cursor < n and s[cursor] in digits:
            s_digits.append(int(s[cursor]))
            cursor += 1
        if s_digits == []:
            return 0
        s_digits.reverse()
        output = 0
        for i in range(len(s_digits)):
            output += s_digits[i] * (10 ** i)
        if negative_bool:
            if output > (2 ** 31):
                output = (2 ** 31)
            output *= -1
        else:
            if output > (2 ** 31) - 1:
                output = (2 ** 31) - 1
        return output
      
    #best space
    class Solution(object):

    def charToDigit(self, c):
        
        if c == '0': return 0
        elif c == '1': return 1
        elif c ==  '2': return 2
        elif c ==  '3': return 3
        elif c ==  '4': return 4
        elif c ==  '5': return 5
        elif c ==  '6': return 6
        elif c ==  '7': return 7
        elif c ==  '8': return 8
        elif c ==  '9': return 9
        else : return -1

    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.strip() # Ignore empty charactres 
        
        if s == "": return 0

        # strings = s.split(" ") # Ignore spaces between strings
        # num = strings[0]
        num = s
        isPositive = True # No sign considered positive
        if num[0] == '-': 
            isPositive = False
            num = num[1:]
        elif num[0] == '+': 
            isPositive = True
            num = num[1:]


        val = 0
        for i in range(len(num)):
            ctod = self.charToDigit(num[i])
            if ctod == -1: break
            val = val * 10 + ctod

        if not isPositive:
            val = val * -1
        
        if isPositive:
            return val if val <= 2**31 -1 else 2**31 - 1
        else:
            return val if val >= -2**31 else -2**31
          
        
