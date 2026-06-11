class Solution:
    MOD = 10**9 + 7

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1

        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        max_depth = 0

        def dfs(node: int, parent: int, depth: int) -> None:
            nonlocal max_depth
            max_depth = max(max_depth, depth)

            for nei in adj[node]:
                if nei != parent:
                    dfs(nei, node, depth + 1)

        dfs(1, 0, 0)

        return pow(2, max_depth - 1, self.MOD)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna