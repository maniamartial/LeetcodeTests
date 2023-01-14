'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



'''
class Solution(object):
    def rotate(self, nums, k):
        if k == 0:
            return nums
        
        # compute rotation
        k = k % len(nums)
        lenght = len(nums)
        
        #swap positions
        nums[lenght-k:], nums[:lenght-k] = nums[:lenght-k],nums[lenght-k:]
        return nums
                
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
