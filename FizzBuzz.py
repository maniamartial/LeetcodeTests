'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

'''

class Solution(object):
    def fizzBuzz(self, n):
        result=[]
        for i in range(1, n+1):
            if i%3==0 and i%5==0:
                result.append("FizzBuzz")
                
            elif i%3==0:
               result.append("Fizz")
                
            elif i%5==0:
                result.append("Buzz")
                
            else:
                result.append(str(i))
                
        return result
      
      
   #best time 8ms
  class Solution(object):
    def fizzBuzz(self, n):
       
        res = []
        for i in range(n):
            if (i+1) % 3 == 0 and (i+1) % 5 == 0:
                res.append("FizzBuzz")
            elif (i+1) % 3 == 0:
                res.append("Fizz")
            elif (i+1) % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i+1))
        return res
      
      
#best 
class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        num = 1
        while num <= n:
            if (num%3 == 0 and num%5 == 0):
                answer.append("FizzBuzz")
                num += 1
            elif num%3 == 0:
                answer.append("Fizz")
                num += 1
            elif num%5 == 0:
                answer.append("Buzz")
                num += 1
            else:
                answer.append(str(num))
                num += 1
        return answer
