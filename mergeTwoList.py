'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#run in 17ms
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
    
 #best space complexity, they used recursive
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        return merge_two_sorted_list(list1, list2)

def merge_two_sorted_list(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val <= list2.val:
        return ListNode(val=list1.val, next=merge_two_sorted_list(list1.next, list2))
    else:
        return ListNode(val=list2.val, next=merge_two_sorted_list(list1, list2.next))


#best space complexity, it took 13mbs
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        current = dummy= ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1= list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next

    
        return new_list
    
   

