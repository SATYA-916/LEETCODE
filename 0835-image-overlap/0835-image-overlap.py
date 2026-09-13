class Solution:
    def largestOverlap(self, m1: List[List[int]], m2: List[List[int]]) -> int:

        def search(m1, m2, x, y):
            s = 0

            for i in range(len(m1)):
                for j in range(len(m1[0])):
                    if 0 <= i + x < len(m2) and 0 <= j + y < len(m2[0]):
                        if m1[i][j] == 1 and m2[i + x][j + y] == 1:
                            s += 1

            return s

        n = len(m1)
        m = 0

        for i in range(-n + 1, n):
            for j in range(-n + 1, n):
                m = max(m, search(m1, m2, i, j))

        return m

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna