from collections import Counter

class Solution(object):
    def maxSubarrayLength(self, nums, k):
        c = Counter()
        i, j, ans = 0, 0, 0

        while j < len(nums):
            c[nums[j]] += 1

            while c[nums[j]] > k:
                c[nums[i]] -= 1
                i += 1

            ans = max(ans, j - i + 1)
            j += 1

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna