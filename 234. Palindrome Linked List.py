# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lister=[]
        while(head!=None):
            lister.append(head.val)
            head=head.next
        reverse=lister[::-1]
        print(lister)
        print(reverse)
        if len(lister)==1:
            return True
        if lister == reverse:
            return True
        return False
            
