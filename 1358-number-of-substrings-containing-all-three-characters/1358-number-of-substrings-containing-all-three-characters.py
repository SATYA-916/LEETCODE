class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = {'a':0, 'b':0, 'c':0}
        l = 0
        ans = 0
        n = len(s)

        for r in range(n):
            cnt[s[r]] += 1

            while cnt['a'] > 0 and cnt['b'] > 0 and cnt['c'] > 0:
                ans += n - r
                cnt[s[l]] -= 1
                l += 1

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna