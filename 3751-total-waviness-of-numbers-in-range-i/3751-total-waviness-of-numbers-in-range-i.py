class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans=0
        for i in range(num1,num2+1):
            x=str(i)
            for j in range(1,len(x)-1):
                print(x[j-1],x[j],x[j+1])
                if (x[j-1]<x[j] and x[j]>x[j+1]) or (x[j-1]>x[j] and x[j]<x[j+1]):
                    ans=ans+1
        return ans



            




        