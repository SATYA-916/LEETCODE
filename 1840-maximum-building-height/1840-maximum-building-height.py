class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])

        if not restrictions or restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        restrictions.sort()

        left = [h for _, h in restrictions]
        right = [h for _, h in restrictions]

        # left -> right (increasing limit)
        for i in range(1, len(restrictions)):
            d = restrictions[i][0] - restrictions[i - 1][0]
            left[i] = min(left[i], left[i - 1] + d)

        # right -> left (decreasing limit)
        for i in range(len(restrictions) - 2, -1, -1):
            d = restrictions[i + 1][0] - restrictions[i][0]
            right[i] = min(right[i], right[i + 1] + d)

        # final valid heights
        h = [min(left[i], right[i]) for i in range(len(left))]

        ans = 0

        for i in range(1, len(restrictions)):
            x1 = restrictions[i - 1][0]
            x2 = restrictions[i][0]

            h1 = h[i - 1]
            h2 = h[i]

            d = x2 - x1

            ans = max(ans, (h1 + h2 + d) // 2)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna