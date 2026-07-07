class Solution:
    def sumAndMultiply(self, n: int) -> int:
        c,x,s=1,0,0
        while(n):
            a=n%10
            if a==0:
                n=n//10
                continue
            s+=a
            n=n//10
            x=a*c+x
            c=c*10
        return x*s     

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna