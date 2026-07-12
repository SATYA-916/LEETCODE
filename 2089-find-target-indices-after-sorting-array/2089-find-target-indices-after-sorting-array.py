class Solution:
    def targetIndices(self, arr: List[int], t: int) -> List[int]:
        c=0
        for i in arr:
            if i==t:
                c+=1
        x=0
        for i in arr:
            if i<t:
                x+=1
        res=[x]
        if c==0:
            return []
        elif c==1:
            return res
        else:
            ans=[]
            for i in range(c-1):
                res.append(res[-1]+1)
            return res

        