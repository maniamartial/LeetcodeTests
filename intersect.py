

'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


'''

class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        
        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1
        return ans
        '''new_array=[]
        if len(nums2)>len(nums1):
            for k in nums1:
                if k in nums2:
                    new_array.append(k)
        elif len(nums1)>len(nums2):
            for k in nums2:
                if k in nums1:
                    new_array.append(k)
                    
        elif len(nums1)==len(nums2):
            already_compaired=[]
            for m in nums1:
                if m in nums2:
                    new_array.append(m)
                    nums1.pop(m)
                    
                    
                    
        return new_array'''
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
