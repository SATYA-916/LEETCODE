class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
        e,o=0,0
        for i in range(1,n*2+1):
            if i%2==0:
                e+=i
            else:
                o+=i
        for j in range(min(e,o),-1,-1):
            if e%j==0 and o%j==0:
                return j

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna