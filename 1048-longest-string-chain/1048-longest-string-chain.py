class Solution:
    def longestStrChain(self, w: List[str]) -> int:
        d, m = {}, float('-inf')

        def good(a, b):
            if len(b) != len(a) + 1:
                return False
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                j += 1
            return i == len(a)

        for i in w:
            if len(i) in d:
                d[len(i)].append(i)
            else:
                d[len(i)] = [i]

        @cache
        def help(x, y):
            if len(x) + 1 not in d:
                return y
            ans = y
            for i in d[len(x) + 1]:
                if good(x, i):
                    ans = max(help(i, y + 1), ans)
            return ans

        for i in w:
            m = max(m, help(i, 0))
        return m+1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna