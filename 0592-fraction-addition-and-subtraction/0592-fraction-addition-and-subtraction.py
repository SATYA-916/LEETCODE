from fractions import Fraction
class Solution:
    def fractionAddition(self, ex: str) -> str:
        x=eval(ex)
        if x==int(x):
            return str(int(x))+"/1"
        return str(Fraction(x).limit_denominator())
        # s=""
        # if x<=1:
        #     if x==int(x):
        #         return str(int(x))+"/1"
        #     if x!=0:
        #         x=1/x
        #     if x>0:
        #         s="1/"+str(math.ceil(x))
        #         return s
        #     else:
        #         s="-1/"+str(abs(math.ceil(x)-1))
        #         return s


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna