class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s,p=0,1
        for i in str(n):
            s+=int(i)
            p*=int(i)
        return n%(s+p)==0
    


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna