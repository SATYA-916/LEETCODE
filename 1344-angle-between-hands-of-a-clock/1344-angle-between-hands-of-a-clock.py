class Solution:
    def angleClock(self, h: int, m: int) -> float:
        hour_angle = (h % 12) * 30 + m * 0.5
        minute_angle = m * 6

        diff = abs(hour_angle - minute_angle)

        return min(diff, 360 - diff)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna