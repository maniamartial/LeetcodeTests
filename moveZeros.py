
'''


'''

class Solution(object):
    def moveZeroes(self, nums):
      #this is my solution but it failed the test oon leetcode, but whne i test on other platform codeeditors, it passes
        '''new_array=[]
        new_array_zero=[]
        for i in nums:
            if i!=0:
                new_array.append(i)
            if i==0:
                new_array_zero.append(i)
                
        return new_array + new_array_zero
        '''
        #this code
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0
            
        return nums
    
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
      
  #best solution for space complexity    
  class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        temp = 0
        numberOfZeros = 0

        if 0 not in nums:
            return

        for index, value in enumerate(nums):
            
            if value == 0:    
                numberOfZeros += 1

        for x in range(0, numberOfZeros):
            nums.remove(0)
            nums.append(0)
        
