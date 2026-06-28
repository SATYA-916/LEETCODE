class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, n: List[int]) -> int:
        n.sort()
        n[0]=1
        for i in range(len(n)):
            if n[i]-n[i-1]>1:
                n[i]=n[i-1]+1
        return max(n)



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna