class Solution:
    def maxNumberOfFamilies(self, n: int, r: List[List[int]]) -> int:
        r.sort()
        l=[0]*11
        l[r[0][1]]=1
        m=r[0][0]
        i=1
        ans = 2 * (r[0][0] - 1)
        if i<len(r):
            while(i<len(r)):
                while i<len(r) and r[i][0]==m:#same row
                    l[r[i][1]]=1
                    i+=1
                if sum(l[2:6])==0 and sum(l[6:10])==0:
                    ans+=2
                elif sum(l[2:6])==0 or sum(l[6:10])==0 or sum(l[4:8])==0:
                    ans+=1
                if i==len(r):
                    break
                ans+=(r[i][0]-m-1)*2
                m=r[i][0]
                l=[0]*11
        else:
            if sum(l[2:6]) == 0 and sum(l[6:10]) == 0:
                ans += 2
            elif sum(l[2:6]) == 0 or sum(l[6:10]) == 0 or sum(l[4:8]) == 0:
                ans += 1
        return ans+(n-r[-1][0])*2











# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna