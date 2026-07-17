from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Frequency of each number
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = number of elements divisible by d
        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for multiple in range(d, mx + 1, d):
                cnt[d] += freq[multiple]

        # exact[d] = number of pairs whose gcd is exactly d
        exact = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            c = cnt[d]
            pairs = c * (c - 1) // 2
            multiple = 2 * d
            while multiple <= mx:
                pairs -= exact[multiple]
                multiple += d
            exact[d] = pairs

        # Prefix sums of pair counts
        prefix = [0] * (mx + 1)
        for d in range(1, mx + 1):
            prefix[d] = prefix[d - 1] + exact[d]

        ans = []
        for q in queries:
            # q is 0-indexed, prefix stores cumulative pair counts
            ans.append(bisect_right(prefix, q))
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna