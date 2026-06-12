class Solution:
    def assignEdgeWeights(self, edges, queries):
        MOD = 10**9 + 7

        n = len(edges) + 1
        LOG = (n).bit_length()

        # Build tree
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Binary lifting tables
        depth = [0] * (n + 1)
        up = [[0] * LOG for _ in range(n + 1)]

        def dfs(node, parent):
            up[node][0] = parent

            for j in range(1, LOG):
                up[node][j] = up[up[node][j - 1]][j - 1]

            for nei in graph[node]:
                if nei != parent:
                    depth[nei] = depth[node] + 1
                    dfs(nei, node)

        dfs(1, 0)

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            # Lift u up
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff & (1 << j):
                    u = up[u][j]

            if u == v:
                return u

            # Lift both
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]

            return up[u][0]

        # Precompute powers of 2
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = []

        for u, v in queries:
            p = lca(u, v)

            k = depth[u] + depth[v] - 2 * depth[p]

            if k == 0:
                ans.append(0)
            else:
                ans.append(pow2[k - 1])

        return ans