from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]):

        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        q = deque([1])
        visited = set([1])

        ans = float("inf")

        while q:
            node = q.popleft()

            for nei, wt in graph[node]:
                ans = min(ans, wt)

                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return ans