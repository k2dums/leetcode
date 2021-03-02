# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        lists=[]
        p1=head
        while(p1!=None):
            lists.append(p1.val)
            p1=p1.next
        p1=head
        lists=lists[::-1]
        i=0
        while(p1!=None):
            p1.val=lists[i]
            i+=1
            p1=p1.next
        return head
