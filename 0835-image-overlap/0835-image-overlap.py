from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        n = len(img2)

        one = []
        on = []

        for i in range(n):
            for j in range(n):
                if img2[i][j] == 1:
                    one.append((i, j))

                if img1[i][j] == 1:
                    on.append((i, j))

        d = defaultdict(int)

        for i in one:
            for j in on:
                d[(j[0] - i[0], j[1] - i[1])] += 1

        return max(d.values(), default=0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna