class Solution:
    def findComplement(self, n: int) -> int:
        x,j=0,0
        if n==0:
            return 1
        while(n):
            if n&1==0:
                temp=1<<j
                x=temp|x
            j+=1
            n=n>>1
        return x

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna