class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d={}
        for i in points:
            x,y=i
            if (abs(x)**2)+(abs(y)**2) in d:
                d[(abs(x)**2)+(abs(y)**2)].append([x,y])
            else:
                d[(abs(x)**2)+(abs(y)**2)]=[[x,y]]
        d = dict(sorted(d.items()))
        ans=[]
        for i in d:
            for j in d[i]:
                ans.append(j)
        return ans[:k]
        
            

