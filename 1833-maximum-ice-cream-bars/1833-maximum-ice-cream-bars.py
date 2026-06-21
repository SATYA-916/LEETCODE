class Solution:
    def maxIceCream(self, cost: List[int], coin: int) -> int:
        ans,pre=[0]*(max(cost)+1),0
        for i in cost:
            ans[i]=ans[i]+1
        i=0
        while(i <len(ans)):
            if ans[i]!=0:
                coin=coin-(i)
                if coin<0:
                    return pre
                pre,ans[i]=pre+1,ans[i]-1
            else:
                i+=1
        return len(cost)

            

        