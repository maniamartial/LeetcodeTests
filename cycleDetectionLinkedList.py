'''

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''

#not my code, linkedlist has been headache to me
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#run in 31ms
class Solution(object):
    def hasCycle(self, head):
          try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

         
        
        
#best time complexity 19ms
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        new_dict = {}
        i = 0
        while curr != None:
            if new_dict.get(curr) is None:
                new_dict[curr] = "Visited"
            else:
                return True
            curr = curr.next
        
        return False
            
        
#best memory consumer used 2100kb
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head:
            if head.val is None: return True
            head.val = None
            head = head.next
        return False

