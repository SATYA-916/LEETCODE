class Solution(object):
    def smallestNumber(self, n, t):
        for i in range(n,10000):
            x=i
            p=1
            while(x):
                p*=x%10
                x=x//10
            if p%t==0:
                return i

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna