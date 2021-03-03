# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            if l1==None and l2==None:
                return l1
            elif l1==None:
                return l2
            elif l2==None:
                return l1
            p1=l1
            p2=l2
            if p1.val<p2.val:
                ans=p1
                p1=p1.next
            else:
                ans=p2
                p2=p2.next
                
            final=ans
            while(p1!=None and p2!=None):
                if p2.val<p1.val:
                    ans.next=p2
                    ans=ans.next
                    p2=p2.next
                    
                else:
                    ans.next=p1
                    ans=ans.next
                    p1=p1.next
                    
            if(p1!=None):
                while(p1!=None):
                    ans.next=p1
                    ans=ans.next
                    p1=p1.next
            else:
                while(p2!=None):
                    ans.next=p2
                    ans=ans.next
                    p2=p2.next
            return final
                    
                    
                    
                
                
