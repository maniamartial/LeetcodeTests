'''

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



'''

class Solution(object):
    def containsDuplicate(self, nums):
        new_array=[]
        result=False
        for i in nums:
            if i not in new_array:
                new_array.append(i)
                
            elif i in new_array:
              
                result=True
                break
        return result
                
        """
        :type nums: List[int]
        :rtype: bool
        """
        
