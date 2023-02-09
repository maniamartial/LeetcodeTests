'''

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.



'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        
        def insert(left, right):
            if left > right:
                return None
            
            mid=(left+right)//2
            root=TreeNode(nums[mid])
            root.left=insert(left, mid-1)
            root.right=insert(mid+1, right)
            
            return root
        return insert(0, len(nums)-1)
      
      
#best time

class Solution(object):
    def sortedArrayToBST(self, num):
        if num:
            mid = len(num) // 2


            root = TreeNode(num[mid])
            root.left = self.sortedArrayToBST(num[0:mid])
            root.right = self.sortedArrayToBST(num[mid+1:len(num)+1])


            return root
        else:


            return None
          
#best memory
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums,0,len(nums)-1)
    def helper(self,nums,low,high):
        if low>high:
            return None
        if low==high :
            return TreeNode(nums[high])
        else:
            middle=(low+high)//2
            return TreeNode(nums[middle],self.helper(nums,low,middle-1),self.helper(nums,middle+1,high))
            
        
