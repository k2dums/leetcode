# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        temp=head
        length_Of_Node=0
        
        while(temp!=None):
            length_Of_Node+=1
            temp=temp.next
        temp=head
        
        node=1
        ref_1=ref_2=head
        flag_1=flag_2=False
        
        while(temp!=None):
            if node==k:
                ref1=temp
                flag_1=True
            if node==length_Of_Node-k+1:
                ref2=temp
                flag_2=True
            if flag_1 and flag_2:
                temp_val=ref1.val
                ref1.val=ref2.val
                ref2.val=temp_val
                return head
            temp=temp.next
            node+=1
