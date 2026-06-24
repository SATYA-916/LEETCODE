from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        # if n<3:
        #     return n
        # a,b=1,1
        # for i in range(n):
        #     a,b=b,b+a
        # return a
        @cache
        def help(x):
            if x<=1:
                return 1
            return help(x-1)+help(x-2)
        return help(n)
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna