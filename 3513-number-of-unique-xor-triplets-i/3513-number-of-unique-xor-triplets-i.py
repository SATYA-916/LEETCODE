class Solution:
    def uniqueXorTriplets(self, nu: List[int]) -> int:
        n=len(nu)
        if n<=2:
            return n
        return 2**n.bit_length()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna