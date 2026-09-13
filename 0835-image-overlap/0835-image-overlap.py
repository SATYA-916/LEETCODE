class Solution:
    def largestOverlap(self, m1: List[List[int]], m2: List[List[int]]) -> int:
        if len(m1)==1 and len(m1[0])==1 and len(m2)==1 and len(m2[0])==1:
            return m1[0][0] and m2[0][0]
        def search(m1,m2,x,y):
            s=0
            n=len(m1)
            for i in range(len(m2)):
                for j in range(len(m2[0])):
                    if 0<=i+x<n and 0<=j+y<n and m1[i][j]+m2[i+x][j+y]==2:
                        s+=1
            return s
        m=0
        n=len(m1)
        for i in range(-n+1,len(m1)):
                for j in range(-n+1,len(m1[0])):
                    m=max(m,search(m1,m2,i,j))
        return m



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna