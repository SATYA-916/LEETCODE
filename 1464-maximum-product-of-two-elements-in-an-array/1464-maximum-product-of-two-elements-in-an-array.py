class Solution:
    def maxProduct(self, n: List[int]) -> int:
        n.sort()

        return (n[-1]-1)*(n[-2]-1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna