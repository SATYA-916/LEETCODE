class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        i = 0
        ans = 0

        while i + k <= len(s):

            # Check length k
            if s[i:i+k] == s[i:i+k][::-1]:
                ans += 1
                i += k

            # Check length k+1
            elif i + k + 1 <= len(s) and s[i:i+k+1] == s[i:i+k+1][::-1]:
                ans += 1
                i += k + 1

            else:
                i += 1

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna