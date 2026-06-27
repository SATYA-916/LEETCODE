class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x,ans,re,j=bin(n)[2:],"",0,0
        for i in x:
            if int(i)==0:
                ans=ans+'1'
            else:
                ans=ans+'0'
        for i in range(len(ans)-1,-1,-1):
            if ans[i]=='1':
                re=re+(2**j)
            j+=1
        return re


        