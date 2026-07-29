from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        half = {}
        mid = ""
        total = 0

        for c in sorted(cnt):
            half[c] = cnt[c] // 2
            total += half[c]
            if cnt[c] % 2:
                mid = c

        def ways(freq, rem):
            ans = 1
            left = rem
            for c in freq:
                f = freq[c]
                if f:
                    ans *= comb(left, f)
                    if ans > k:
                        return ans
                    left -= f
            return ans

        if ways(half, total) < k:
            return ""

        first = []

        while total:
            for ch in sorted(half):
                if half[ch] == 0:
                    continue

                half[ch] -= 1
                cntWays = ways(half, total - 1)

                if cntWays >= k:
                    first.append(ch)
                    total -= 1
                    break
                else:
                    k -= cntWays
                    half[ch] += 1

        left = "".join(first)
        return left + mid + left[::-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna