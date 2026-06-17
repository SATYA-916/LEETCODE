class Solution:
    def reverseWords(self, s: str) -> str:
        ans,x=s.strip(),""
        for i in ans.split()[::-1]:
            x=x+" "+i
        return x[1:]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna