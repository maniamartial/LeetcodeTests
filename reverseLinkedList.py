'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#run with 18ms
class Solution(object):
    def reverseList(self, head):
        prev=None
        curr=head
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev
 


#best time complexity run with 8ms
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #return head

        if(head is None): #empty linked list
            return
    
        cur=head

        while(cur.next):

            node=cur.next  
            cur.next=cur.next.next #point to the one after the next

            node.next=head
            head=node
            
       return head

#best space complexity
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        t = None
        c = head
        p = None
        while c:
            t = c.next
            c.next = p
            p = c
            c = t
        return p
             
