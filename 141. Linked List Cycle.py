# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head==None or head.next==None:
            return False
        lister=[]
        while(head!=None):
            if head not in lister:
                lister.append(head)
            else:
                return True
            head=head.next
        return False
