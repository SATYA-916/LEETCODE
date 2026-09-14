class Solution:
    def isRectangleOverlap(self, r1: List[int], r2: List[int]) -> bool:
        x1=max(r1[0],r2[0])
        x2=min(r1[2],r2[2])
        y1=max(r1[1],r2[1])
        y2=min(r1[3],r2[3])
        return x1<x2 and y1<y2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna