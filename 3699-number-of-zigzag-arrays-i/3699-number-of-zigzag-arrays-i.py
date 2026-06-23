class Solution:
    def zigZagArrays(self, n: int, lo: int, r: int) -> int:
        nums = list(range(lo, r + 1))
        ans = 0

        def valid(arr):
            if len(arr) < 3:
                return True

            a, b, c = arr[-3], arr[-2], arr[-1]

            if a < b < c:
                return False
            if a > b > c:
                return False

            return True

        def dfs(cur):
            nonlocal ans

            if len(cur) == n:
                ans += 1
                return

            for x in nums:
                if cur and x == cur[-1]:
                    continue

                cur.append(x)

                if valid(cur):
                    dfs(cur)

                cur.pop()

        dfs([])
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna