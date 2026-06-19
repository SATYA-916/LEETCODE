class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        c=gain[0]
        ans=gain[0]
        for i in range(1,len(gain)):
            ans=ans+gain[i]
            c=max(c,ans)
        return max(c,0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna