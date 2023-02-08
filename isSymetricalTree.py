'''

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        
        stack=[[root.left, root.right]]
        while stack:
            left, right=stack.pop()
            if left is None and right is None:
                continue
                
            if left is None or right is None:
                return False
            
            if left.val != right.val:
                return False
            
            stack.append([left.left, right.right])
            stack.append([left.right, right.left])
            
        return True

      
    #best time 3ms
    
    def symm(left, right):
    if ((not left and not right)):
        return True
    if (((left and right) and (left.val == right.val))):
        if (not symm(left.left, right.right)):
            return False
        if (not symm(left.right, right.left)):
            return False
        return True
    return False

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return symm(root.left, root.ri
                    
                    
    #best memory 13300kb
                    
 class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(a,b):
            if a==None and b==None:return True
            if a==None or b==None or a.val!=b.val:return False
            return dfs(a.left,b.right) and dfs(a.right,b.left)
        return dfs(root.left,root.right)
        
        
