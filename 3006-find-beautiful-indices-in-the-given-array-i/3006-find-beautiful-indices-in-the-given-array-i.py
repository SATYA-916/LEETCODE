class Solution(object):
    def beautifulIndices(self, s, a, b, k):
        """
        :type s: str
        :type a: str
        :type b: str
        :type k: int
        :rtype: List[int]
        """
        aoc=[]
        boc=[]
        for i in range(len(s)-len(a)+1):
            if s[i:i+len(a)]==a:
                aoc.append(i)
        for i in range(len(s)-len(b)+1):
            if s[i:i+len(b)]==b:
                boc.append(i)
        i,j=0,0
        res=[]
        print(aoc,boc)
        while j<len(boc) and i<len(aoc):
            if abs(aoc[i]-boc[j])<=k:
                res.append(aoc[i])
                i+=1
            elif boc[j]<aoc[i]:
                j+=1
            else:
                i+=1
        return res


        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna