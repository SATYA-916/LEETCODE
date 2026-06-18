class Solution:
    def angleClock(self, h: int, m: int) -> float:
        hour_angle = (h % 12) * 30 + m * 0.5
        minute_angle = m * 6

        diff = abs(hour_angle - minute_angle)

        return min(diff, 360 - diff)