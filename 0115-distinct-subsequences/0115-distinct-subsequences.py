class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def help(i,j,s,t):
            if j>=len(t):
                return 1
            if i>=len(s):
                return 0
            if s[i]==t[j]:
                return (help(i+1,j+1,s,t)+help(i+1,j,s,t))
            return help(i+1,j,s,t)
        return help(0,0,s,t)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna