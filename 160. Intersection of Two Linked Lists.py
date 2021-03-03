# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA==None or headB==None:
            return None
        p1=headA
        p2=headB
        flaga=True
        flagb=True
        while(p1!=None or p2!=None):
            if p1==p2:
                return p1
            if p1.next==None and flaga:
                p1=headB
                flaga=False
            else:
                 p1=p1.next
            if p2.next==None and flagb:
                p2=headA
                flagb=False
            else:
                 p2=p2.next
           
           
        return None
        
