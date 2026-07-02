class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k-=1
        ans=""
        l=[]
        for i in range(1,n+1):
            l.append(str(i))
        for x in range(n-1,-1,-1):
            ans=ans+l[k//factorial(x)]
            l.pop(k//factorial(x))
            k=k%factorial(x)
        return ans