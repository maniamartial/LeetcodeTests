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
        
        
        '''the least memory used and accepted answer was this'''
  class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False;
    
    
    '''accepted solution that took the least time '''
    class Solution(object):
        def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
            hashNum={}
            for i in nums:
                if i not in hashNum:
                    hashNum[i] = 1
                else:
                    return True
                
            return False

        #Dictionarry are musch faster as compaired to list, they are lookup, while list are iteration
        #when compairing about space, dictinary occupies ore space hence list becomes best options
        
