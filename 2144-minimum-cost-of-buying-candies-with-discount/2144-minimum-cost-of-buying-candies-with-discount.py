class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        a=2
        s=0
        print(cost)
        for i in cost[::-1]:
            if a==0:
                a=2
                continue
            s=s+i
            a=a-1
        return s
