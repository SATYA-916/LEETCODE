import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        p=[]
        m=float('-inf')
        for i in nums:
            m=max(m,i)
            p.append(math.gcd(i,m))
        p.sort()
        ans=0
        for i in range(len(p)//2):
            ans+=math.gcd(p[i],p[len(p)-i-1])
        return ans




        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna