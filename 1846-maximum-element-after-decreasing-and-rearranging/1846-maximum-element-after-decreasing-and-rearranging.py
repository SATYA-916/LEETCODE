class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, n: List[int]) -> int:
        n.sort()
        n[0]=1
        for i in range(len(n)):
            if n[i]-n[i-1]>1:
                n[i]=n[i-1]+1
        return max(n)



        