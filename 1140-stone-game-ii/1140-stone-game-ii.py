class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def help(i, m):
            if i >= n:
                return 0

            if (i, m) in memo:
                return memo[(i, m)]

            best = 0
            taken = 0

            # Take X piles, where 1 <= X <= 2*M
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break

                taken += piles[i + x - 1]

                new_m = max(m, x)

                # Opponent gets the best they can get
                opponent = help(i + x, new_m)

                # Current player gets everything else
                current = suffix[i] - opponent

                best = max(best, current)

            memo[(i, m)] = best
            return best

        return help(0, 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna