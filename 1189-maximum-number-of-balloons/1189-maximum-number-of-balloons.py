class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s="balloon"
        d={}
        m=float('inf')
        for i in s:
            d[i]=0
        for i in text:
            if i in d:
                d[i]=d[i]+1
        for i in d:
            m=min(m,d[i])
        return min(m,d['o']//2,d['l']//2)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna