class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        s=set()
        for i in bank:
            s.add(i)

        i,j,ans=0,len(start)-1,0

        while(start[i]==end[i]):
            i=i+1

        while(start[j]==end[j]):
            j=j-1

        while(i<=j):
            if start==end:
                return ans

            if (start[:i]+end[i]+start[i+1:]) in s:
                print("i is increment",start,start[:i]+end[i]+start[i+1:])
                ans=ans+1
                start=start[:i]+end[i]+start[i+1:]
                i=i+1

            elif (start[:j]+end[j]+start[j+1:]) in s:
                print("j is dec",start,start[:j]+end[j]+start[j+1:])
                ans=ans+1
                start=start[:j]+end[j]+start[j+1:]
                j=j-1

            else:
                return -1

        return ans if start == end else -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna