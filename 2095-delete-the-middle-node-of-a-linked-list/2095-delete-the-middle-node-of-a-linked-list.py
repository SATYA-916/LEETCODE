# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        t=head
        if head.next==None:
            return None
        while(t):
            c+=1
            t=t.next
        c=c//2
        t=head
        while(c-1!=0 and t):
            t=t.next
            c-=1
        t.next=t.next.next
        return head


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna