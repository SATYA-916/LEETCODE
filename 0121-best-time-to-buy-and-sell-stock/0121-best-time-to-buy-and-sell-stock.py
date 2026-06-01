class Solution:
    def maxProfit(self, p: List[int]) -> int:
        best = p[0]
        pr = 0
        for i in range(1, len(p)):
            best=min(best,p[i])
            pr=max(pr,p[i]-best)
        return pr
