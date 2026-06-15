# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=head
        f=head
        if head is None or head.next is None:
            return None
        while(f and f.next):
            pr=s
            s=s.next
            if f.next:
                f=f.next.next
            else:
                f=f.next
        if pr!=None:
            print(pr.val)
            pr.next=pr.next.next
            print(pr.val)
        return head


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna