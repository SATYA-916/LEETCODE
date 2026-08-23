class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)

        lf = rt = 0
        lq = rq = 0

        for i in range(n):
            if num[i] == '?':
                if i < n // 2:
                    lq += 1
                else:
                    rq += 1
            else:
                if i < n // 2:
                    lf += int(num[i])
                else:
                    rt += int(num[i])

        return 2 * (lf - rt) + 9 * (lq - rq) != 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna