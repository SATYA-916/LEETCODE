from collections import Counter
class Solution(object):
    def maximumLengthSubstring(self, s):
        c=Counter(s)
        for i in c:
            c[i]=0
        i,j,ans=0,0,0
        while(j<len(s)):
            if c[s[j]]<2:
                ans=max(ans,j-i+1)
                c[s[j]]+=1
                j+=1
            else:
                c[s[i]]-=1
                i+=1
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna