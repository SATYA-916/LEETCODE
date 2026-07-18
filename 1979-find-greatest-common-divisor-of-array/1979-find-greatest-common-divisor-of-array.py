class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def h(a,b):
            if b==0: return a
            return h(b,a%b)
        return h(max(nums),min(nums))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna