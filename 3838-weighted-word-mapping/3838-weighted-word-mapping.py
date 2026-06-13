class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        l=[]
        for i in range(ord('z'),ord('a')-1,-1):
            l.append(chr(i))
        temp,ans,j=0,"",0
        for i in words:
            for k in i:
                temp=temp+weights[ord(k)-ord('a')]
                j=j+1
            ans=ans+l[temp%26]
            temp=0
        return ans
                

        