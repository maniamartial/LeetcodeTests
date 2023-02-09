'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Sol generated by chatGPT, runtime 15ms

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        
        result=[]
        queue=deque([root])
        while queue:
            level=[]
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            result.append(level)
            
        return result
      
      
   #best time 5ms
  class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: 
          return []
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
        
        return res
      
      
      #best memory 13400kb
      
 class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        level = [root]
        while len(level):
            ans.append([node.val for node in level if node])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return ans
      

      
      
  
