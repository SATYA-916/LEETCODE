class Solution:
    def numberOfSets(self, n: int, k: int) -> int:

        m = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):

            dp[i][0] = 1

            # if k==0:
            #     return 1

            # if i>=n:
            #     return 0

        for K in range(1, k + 1):

            suffix = [0] * (n + 1)

            for i in range(n - 1, -1, -1):
                suffix[i] = (suffix[i + 1] + dp[i][K - 1]) % m

            for i in range(n - 1, -1, -1):

                # skip=solve(i+1,k)
                skip = dp[i + 1][K]

                # take=0
                # for j in range(i+1,n):
                #     take+=solve(j,k-1)

                take = suffix[i + 1]

                dp[i][K] = (take + skip) % m

        return dp[0][k] % m

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna