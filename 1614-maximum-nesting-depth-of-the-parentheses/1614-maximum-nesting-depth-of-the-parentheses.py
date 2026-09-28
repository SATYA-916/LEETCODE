class Solution:
    def maxDepth(self, s: str) -> int:
        l=[]
        m=0
        for i in s:
            if i=='(':
                l.append(i)
                m=max(m,len(l))
            if i==')':
                l.pop()
        return m

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna