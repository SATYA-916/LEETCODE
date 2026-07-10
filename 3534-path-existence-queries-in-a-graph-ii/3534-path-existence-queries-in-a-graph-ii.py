from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Sort (value, original_index)
        arr = sorted((nums[i], i) for i in range(n))

        # pos[original_index] = position in sorted array
        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        # Component ID for each sorted position
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if arr[i][0] - arr[i - 1][0] > maxDiff:
                cid += 1
            comp[i] = cid

        # next_right[i] = farthest position reachable in one jump
        next_right = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and arr[j + 1][0] - arr[i][0] <= maxDiff:
                j += 1
            next_right[i] = j

        # Binary lifting
        LOG = n.bit_length()
        up = [next_right]

        for _ in range(1, LOG):
            prev = up[-1]
            curr = [0] * n
            for i in range(n):
                curr[i] = prev[prev[i]]
            up.append(curr)

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            pu = pos[u]
            pv = pos[v]

            if pu > pv:
                pu, pv = pv, pu

            # Different connected components
            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue

            jumps = 0
            cur = pu

            # Binary lifting to make maximum jumps without passing pv
            for k in range(LOG - 1, -1, -1):
                nxt = up[k][cur]
                if nxt < pv:
                    cur = nxt
                    jumps += 1 << k

            ans.append(jumps + 1)

        return ans