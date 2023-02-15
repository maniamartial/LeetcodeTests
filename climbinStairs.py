'''

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

'''

class Solution(object):
    def climbStairs(self, n):
        if n==1:
            return 1
            
        elif n==2:
            return 2
            
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        
        for i in range(3, n+1):
            dp[i]=dp[i-1]+dp[i-2]
            
        return dp[n]

    
    
    #best time 0ms
 class Solution(object):
    def climbStairs(self, n):
      
        if n <= 3:
            return n
        i = 2
        j = 3
        k = 4
        ans = 0
        while k <= n:
            ans = i + j
            i = j
            j = ans
            k += 1
        return ans
      
  #best memory 13500kb
  class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n==1 or n==0:
            return 1
        else:
            a=[1]*(n+1)
            for i in range(2,n+1):
                a[i]=a[i-1]+a[i-2]
            return a[n] 
  
