class Solution:
    def maximumProduct(self, n: List[int]) -> int:
        n.sort()
        return max(n[-1]*n[-2]*n[-3],n[-1]*n[0]*n[1])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna