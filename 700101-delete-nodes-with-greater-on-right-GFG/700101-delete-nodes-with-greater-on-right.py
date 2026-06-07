class Solution:
    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def compute(self, head):
        head = self.reverse(head)

        mx = head.data
        curr = head

        while curr and curr.next:
            if curr.next.data < mx:
                curr.next = curr.next.next
            else:
                curr = curr.next
                mx = curr.data

        return self.reverse(head)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna