# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fp=sp=head
        while(fp!=None and fp.next!=None):
            sp=sp.next
            fp=fp.next.next   
        return sp
            
