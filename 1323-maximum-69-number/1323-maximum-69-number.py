class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        for i in range(len(s)):
            if s[i]=='6':
                return int(s[:i]+"9"+s[i+1:])
        return num

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna