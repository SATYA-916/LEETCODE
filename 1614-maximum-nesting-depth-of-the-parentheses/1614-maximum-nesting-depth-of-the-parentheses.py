class Solution:
    def maxDepth(self, s: str) -> int:
        l=0
        m=0
        for i in s:
            if i=='(':
                l+=1
                m=max(m,l)
            if i==')':
                l-=1
        return m

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna