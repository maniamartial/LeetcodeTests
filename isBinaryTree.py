'''

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Done with chatGPT
class Solution(object):
    def isValidBST(self, root):
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            
            val = node.val
            
        #compairing the value on the left if its smaller than the parent(root) and value on right is greater than the root
            if val <= lower or val >= upper:
                return False
            
            
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

#best time 
class Solution(object):
    def isValidBST(self, root):
        stack = []
        curr = root
        prevVal = float('-inf')
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                if node.val <= prevVal:
                    return False
                prevVal = node.val
                curr = node.right
        return True
      
      
 #17500kb
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [(root, -float('inf'), float('inf'))]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True
