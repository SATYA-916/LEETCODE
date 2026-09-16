class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        @cache
        def solve(a, x):
            if x == 0:
                return 1
            if a == n - 1:
                return 0

            return (solve(a + 1, x) + suffix(a + 1, x - 1)) % MOD

        @cache
        def suffix(a, x):
            if a == n:
                return 0
            return (solve(a, x) + suffix(a + 1, x)) % MOD

        return solve(0, k)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna