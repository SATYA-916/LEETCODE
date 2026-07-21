class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"
        ones = s.count('1')
        n = len(t)

        blocks = []
        i = 0

        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            blocks.append((t[i], j - i))
            i = j

        ans = ones

        for i in range(1, len(blocks) - 1):
            if (blocks[i][0] == '1' and
                blocks[i - 1][0] == '0' and
                blocks[i + 1][0] == '0'):
                gain = blocks[i - 1][1] + blocks[i + 1][1]
                ans = max(ans, ones + gain)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna