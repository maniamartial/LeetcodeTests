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
        

        #my other solution that runs., but the testcase doesn't work on 
        
"""
nums=[1,2,3,4,5,6,7]

new_array=[]
k=3
for m in range(k):
    first=nums.pop()
    new_array.append(first)
    reverse=new_array[::-1]
    #nums.append(first)
    
print(reverse+nums)"""
