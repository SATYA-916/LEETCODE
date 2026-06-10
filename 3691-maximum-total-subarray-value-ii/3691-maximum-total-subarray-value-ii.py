
from heapq import heappush, heappop
from math import log2
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        LOG = n.bit_length()

        mx = [nums[:]]
        mn = [nums[:]]

        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1

            mx.append([
                max(mx[j-1][i], mx[j-1][i+half])
                for i in range(n-length+1)
            ])

            mn.append([
                min(mn[j-1][i], mn[j-1][i+half])
                for i in range(n-length+1)
            ])
            j += 1

        def value(l, r):
            length = r - l + 1
            p = length.bit_length() - 1

            mxv = max(mx[p][l], mx[p][r-(1<<p)+1])
            mnv = min(mn[p][l], mn[p][r-(1<<p)+1])

            return mxv - mnv

        heap = []

        for l in range(n):
            heappush(heap, (-value(l, n-1), l, n-1))

        ans = 0

        for _ in range(k):
            negv, l, r = heappop(heap)
            ans += -negv

            if r > l:
                heappush(heap, (-value(l, r-1), l, r-1))

        return ans