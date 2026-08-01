from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]):

        def help(i, j, p1, p2, turn):
            if i > j:
                return p1 >= p2

            if turn == 0:
                return (help(i + 1, j, p1 + nums[i], p2, 1) or
                        help(i, j - 1, p1 + nums[j], p2, 1))
            else:
                return (help(i + 1, j, p1, p2 + nums[i], 0) and
                        help(i, j - 1, p1, p2 + nums[j], 0))

        return help(0, len(nums) - 1, 0, 0, 0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna