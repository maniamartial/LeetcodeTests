'''


'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        
        #find length of the middle num
        length=0
        middle=head
        current=head
        while current:
            current=current.next
            length+=1
            if length % 2 == 0:
                middle = middle.next
                
                
    #Reverse the second half
        prev=None
        current=middle
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next
            
            
#compare the first half and the reversed
        first=head
        second=prev
        for i in range(length//2):
            if first.val != second.val:
                return False
            first=first.next
            second=second.next
            
#Re-reverse the second  
        prev=None
        current=prev
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=prev
            
        middle=prev
        
        return True
    
         
    
   #best time 642ms
  # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s=head
        f=head
        rev=None
        while(f is not None and f.next is not None):
            f=f.next.next
            t=s
            s=s.next
            t.next=rev
            rev=t
        if(f is not None):
            s=s.next
        while(s is not None):
            if(s.val!=rev.val):
                return False
            s=s.next
            rev=rev.next
        return True
      
      
        
    
#space complexity
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = head; f = head; p = None
        while f and f.next:
            f = f.next.next
            p, p.next, s = s, p, s.next
        if f:
            s = s.next
        while p and p.val == s.val:
            p = p.next
            s = s.next
        return not p
    
        
    
        
