'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''

#time 18ms
class Solution(object):
    def firstBadVersion(self, n):
        left=1
        right=n
        
        while left < right:
            mid=left + (right - left)//2
            if isBadVersion(mid):
                right=mid
                
            else:
                left=mid+1
                
        return left
      
#best time complexity rum 0ms
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        high=n
        mid=(low+high)//2
        
        while low<=high:
            if isBadVersion(mid):
                high=mid-1
                mid=(low+high)//2
            else:
                low=mid+1
                mid=(low+high)//2
        if isBadVersion(low):
            return low
        else:
            return high
       
      
#best space complexity 12900kb
class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        result = 1
        
        while left <= right:
            mid = (left+right)//2
            if isBadVersion(mid) == False:
                left = mid+1
            else:
                right = mid-1
                result = mid
                
        return result


 
