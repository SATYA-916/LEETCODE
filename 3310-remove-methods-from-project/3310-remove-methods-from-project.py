class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """

        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        suspicious = [False] * n

        def dfs(node):
            if suspicious[node]:
                return

            suspicious[node] = True

            for nei in graph[node]:
                dfs(nei)

        # Mark all suspicious methods
        dfs(k)

        # Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return [i for i in range(n)]

        ans = []

        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna