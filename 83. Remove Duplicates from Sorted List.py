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
