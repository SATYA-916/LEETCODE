class Solution:
    def processStr(self, s: str) -> str:
        ans=""
        for i in s:
            if i.isalpha():
                ans=ans+i
            if i=='#':
                ans=ans+ans
            if i=='%':
                ans=ans[::-1]
            if i=="*":
                ans=ans[:len(ans)-1]
        return ans




        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna