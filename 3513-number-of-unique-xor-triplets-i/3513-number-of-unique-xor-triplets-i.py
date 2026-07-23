class Solution:
    def uniqueXorTriplets(self, n: List[int]) -> int:
        if len(n)<=2:
            return len(n)
        return 2**len(n).bit_length()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna