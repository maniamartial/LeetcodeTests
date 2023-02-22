'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max=0
        curr_max=0
            
        for num in nums:
            prev_max, curr_max=curr_max, max(prev_max+num, curr_max)
            
        return curr_max
      
#best time complexity
 class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0]=nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return max(dp)
      
#best space complexity
class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) <= 2:
        #     return max(nums)
        # if len(nums) == 3:
        #     return max(nums[0] + nums[2], nums[1])
        nums_copy = [0, 0, 0] + nums[:]
        for i in range(3, len(nums_copy)):
            nums_copy[i] += max(nums_copy[i-2], nums_copy[i-3])
        return max(nums_copy[-1], nums_copy[-2])
      
      
