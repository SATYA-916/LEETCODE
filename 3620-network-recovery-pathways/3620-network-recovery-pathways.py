from collections import deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        adj = [[] for _ in range(n)]
        indeg = [0] * n
        mx = 0

        for u, v, w in edges:
            adj[u].append((v, w))
            indeg[v] += 1
            mx = max(mx, w)

        # Topological order
        topo = []
        q = deque(i for i in range(n) if indeg[i] == 0)

        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        def check(limit):
            INF = 10 ** 18
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in adj[u]:
                    if w < limit:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    dist[v] = min(dist[v], dist[u] + w)

            return dist[n - 1] <= k

        lo, hi = 0, mx
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna