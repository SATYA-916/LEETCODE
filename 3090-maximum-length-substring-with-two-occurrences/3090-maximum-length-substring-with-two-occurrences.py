from collections import Counter
class Solution(object):
    def maximumLengthSubstring(self, s):
        def chk(x):
            c=Counter(x)
            for i in c:
                if c[i]>2:
                    return False
            return True
        i,j,ans=0,0,0
        while(j<len(s)):
            if chk(s[i:j+1]):
                ans=max(ans,j-i+1)
                j+=1
            else:
                i+=1
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna