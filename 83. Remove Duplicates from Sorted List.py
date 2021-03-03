class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None:
            return None
        lists=[]
        final=ans=head
        lists.append(head.val)
        head=head.next
        
        while(head!=None ):
            if head.val not in lists:
                ans.next=head
                lists.append(head.val)
                ans=ans.next
            if head.next!=None and head.next.next==None and head.next.val in lists:
                ans.next=None
            if head.next==None and head.val in lists:
                ans.next=None
            head=head.next
#2nd Method
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         ans=final=head
#         lists=[]
#         #First keeping all the value to a list
#         while(head!=None):
#             lists.append(head.val)
#             head=head.next
#         ############################
        
#         lists=list(set(lists))
#         lists.sort()
#         print(lists)
        
#         for i in range(len(lists)):
#             ans.val=lists[i]
#             if i==len(lists)-1:
#                 ans.next=None
#                 return final
#             ans=ans.next
