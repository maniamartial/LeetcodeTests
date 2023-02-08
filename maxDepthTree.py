'''

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

'''

#my code hit 100% of python submission
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
        
        
        
        """
        :type root: TreeNode
        :rtype: int
        """
        
 #least memory 15600kb
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        res = []
        stack = [root]

        while stack:
            level = []
            children = []
            while stack:
                curr = stack.pop(0)
                level.append(curr.val)
                if curr.left: children.append(curr.left)
                if curr.right: children.append(curr.right)

            res.append(level)
            stack = children
        
        return len(res)
 
