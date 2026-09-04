class Solution:
    def firstStableIndex(self, n: list[int], k: int) -> int:
        ma,mi=[],[]
        maxi=float('-inf')
        mini=float('inf')
        for i in n:
            maxi=max(maxi,i)
            ma.append(maxi)
        for i in n[::-1]:
            mini=min(mini,i)
            mi.append(mini)
        mi=mi[::-1]
        for i in range(len(n)):
            if ma[i]-mi[i]<=k:
                print(ma[i],mi[i],i,k)
                return i
        return -1



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna