class Solution:
    def firstStableIndex(self, n: list[int], k: int) -> int:
        for i in range(len(n)):
            if max(n[:i+1])-min(n[i:])<=k:
                return i
        return -1



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna