'''


Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''

class Solution(object):
    def romanToInt(self, s):
        
    
    #initialize a dictionary with all the numbers
        roman_dict={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result=0
        prev_num=0

        for i in range(len(s)-1, -1, -1):
            
            curr_num=roman_dict[s[i]]
            
            if curr_num < prev_num:
                result-=curr_num

            else:
                result+=curr_num

            prev_num=curr_num

        return result
    
    
       
      
#best 8ms
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        
        return sum(map(lambda i: dict[i], s))
      
#best memory 13200kb
class Solution(object):
    def romanToInt(self, s):
        s += '%'
        roms = {
        'M':1000,
        'CM':900,
        'D':500,
        'CD':400,
        'C':100,
        'XC':90,
        'L':50,
        'XL':40,
        'X':10,
        'IX':9,
        'V':5,
        'IV':4,
        'I':1
        }
        rep = 0
        i = 0
        while s[i] != '%':
            if s[i]+s[i+1] in roms:
                rep += roms[s[i]+s[i+1]]
                i += 2
            else:
                rep += roms[s[i]]
                i += 1
        return rep
      
      
