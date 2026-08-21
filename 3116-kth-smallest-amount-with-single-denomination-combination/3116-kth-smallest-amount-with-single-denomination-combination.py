from math import gcd

class Solution:
    def findKthSmallest(self, coins, k):

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            ans = 0

            for mask in range(1, 1 << len(coins)):
                L = 1
                bits = 0

                for i in range(len(coins)):
                    if mask & (1 << i):
                        bits += 1
                        L = lcm(L, coins[i])

                        if L > x:
                            break

                else:
                    if bits % 2:
                        ans += x // L
                    else:
                        ans -= x // L

            return ans

        low = 1
        high = min(coins) * k

        while low < high:
            mid = (low + high) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna