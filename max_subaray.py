'''


'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #initialize maximum sum
        max_sum=nums[0]
        
        #we keep track of the current sum
        current_sum=nums[0]
        
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum+nums[i])
            max_sum=max(max_sum, current_sum)
            
        return max_sum
    
   #best time complexity 625ms
  class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            if curr_sum > max_sum:
                max_sum = curr_sum
            
        return max_sum
      
 
