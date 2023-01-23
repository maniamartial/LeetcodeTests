'''

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''

import sys
class Solution(object):
    def reverse(self, x):
        x = list(str(x))
        x.reverse()
        if x[-1] == '-':
            x = [x[-1]] + x
            x.pop(-1)
        x = "".join(x)
        if -2**31 <= int(x) <= ((2**31)-1):
            return int(x)
        else:
            return 0
   
        
        
 #best time complexity
class Solution(object):
    def reverse(self, y):
        """
        :type x: int
        :rtype: int
        """
        y = str(y)

        arr =[]        

        for i in range(len(y)):            
            arr.insert(0,y[i])

        if arr[-1] == '-':
            arr = arr[:-1]
            arr.insert(0,"-")

        y = ''.join(arr)
        y = int(y)

        if not (-2**31 <= int(y) <= 2**31-1):
            return 0


        return y
      
#Best spce complexity
class Solution(object):
    def reverse(self, num):
        """
        :type x: int
        :rtype: int
        """
        sum = 0
        sign = 1
        if num<0:
            sign = -1
            num = num*-1
        while num>0:
            rem = num%10
            sum= sum*10+rem
            num=num//10
        if not -2147483647<sum<2147483647-1:
            return 0
        return sign*sum
      
     
