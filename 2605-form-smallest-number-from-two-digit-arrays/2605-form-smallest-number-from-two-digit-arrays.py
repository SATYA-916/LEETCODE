class Solution:
    def minNumber(self, n1: List[int], n2: List[int]) -> int:
        s=set(n1)
        m=float('inf')
        for i in n2:
            if i in s:
                m=min(m,i)
        if m!=float('inf'):
            return m
        return min(
            int(str(min(n1)) + str(min(n2))),
            int(str(min(n2)) + str(min(n1)))
        )

        