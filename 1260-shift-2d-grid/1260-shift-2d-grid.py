class Solution:
    def shiftGrid(self, g: List[List[int]], k: int) -> List[List[int]]:
        k=k%(len(g)*len(g[0]))
        if k==0:
            return g
        a=[]
        for i in g:
            for j in i:
                a.append(j)
        a=a[::-1]
        a=a[:k][::-1]+a[k:][::-1]
        c=0
        print(a)
        for i in range(len(g)):
            for j in range(len(g[0])):
                g[i][j]=a[c]
                c+=1
        return g


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna