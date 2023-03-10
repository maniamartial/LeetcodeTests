'''
Given an integer n, return the number of prime numbers that are strictly less than n.


'''

class Solution:
# @param {integer} n
# @return {integer}
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)
      
      
      
      
#best space 15900kbs
class Solution(object):
    def countPrimes(self, n):
        
        if n <= 2:
            return 0
        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = False
                    j += i
        
        return sum(is_prime)

