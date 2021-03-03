# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
       
        if head==None:
            return None
        while (head!=None and head.val==val ):
            head=head.next
        final=ans=head
                
        
        while(head!=None and head.next!=None):
            if head.next.val!=val:
                ans.next=head.next
                ans=ans.next
            if head.next.val==val and head.next.next==None:
                ans.next=None
            head=head.next
        return final
