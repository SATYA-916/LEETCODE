class Solution:
    def countCompleteComponents(self, n: int, e: List[List[int]]) -> int:
        d = [[] for _ in range(n)]
        edge = 0

        for i in e:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])

        vis = [False] * n
        c = 0

        def dfs(x):
            nonlocal edge
            edge += len(d[x])      # <-- only change here
            for i in d[x]:
                if not vis[i]:
                    vis[i] = True
                    dfs(i)

        for i in range(n):
            if not vis[i]:
                x = vis.copy()
                vis[i] = True
                dfs(i)

                v = 0
                for j in range(len(vis)):
                    if x[j] != vis[j]:
                        v += 1

                edge //= 2          # <-- keep //2

                if edge == (v * (v - 1)) // 2:
                    c += 1

                edge = 0

        return c