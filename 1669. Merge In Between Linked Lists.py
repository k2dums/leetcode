# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        final=list1
        node=0
        while list1!=None:
            if node==a-1:
                temp=list1
                list1=list1.next
                node+=1
                temp.next=list2
            if node==b+1:
                while(list2.next!=None):
                    list2=list2.next
                list2.next=list1
                break      
                
            list1=list1.next
            node+=1

            
        return final
