class Solution:
    def removeCoveredIntervals(self, inter: List[List[int]]) -> int:
        inter.sort(key=lambda x: (x[0], -x[1]))
        m,c=float('-inf'),0
        for i in inter:
            if m<i[1]:
                c+=1
                m=i[1]
        return c

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna