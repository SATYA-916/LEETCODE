class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        comp = [0] * n

        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                comp[i] = comp[i - 1]
            else:
                comp[i] = comp[i - 1] + 1

        return [comp[u] == comp[v] for u, v in queries]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna