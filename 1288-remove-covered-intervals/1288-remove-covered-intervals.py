class Solution:
    def removeCoveredIntervals(self, inter: List[List[int]]) -> int:
        c=0
        for i in range(len(inter)):
            for j in range(len(inter)):
                if i!=j:
                    if inter[j][0]<=inter[i][0] and inter[j][1]>=inter[i][1]:
                        c+=1 
                        break
        return len(inter)-c  