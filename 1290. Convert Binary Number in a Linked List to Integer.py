# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        lists=[]
        while head!=None:
            lists.insert(0,head.val)
            head=head.next
        sums=0
        for i,val in enumerate(lists):
            print(val)
            sums=sums+ val*(2**i)
        return sums     
        
        
        
        
