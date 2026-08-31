class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        head=head.next
        first=-1
        last=-1
        mi=float('inf')
        ma=-1
        i=1
        while head and head.next:
            if (prev.val < head.val and head.val > head.next.val) or \
               (prev.val > head.val and head.val < head.next.val):
                if first==-1:
                    first=i
                else:
                    mi=min(mi,i-last)
                    ma=max(ma,i-first)
                last=i
            prev=head
            head=head.next
            i+=1
        if first==-1 or first==last:
            return [-1,-1]
        return [mi,ma]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna