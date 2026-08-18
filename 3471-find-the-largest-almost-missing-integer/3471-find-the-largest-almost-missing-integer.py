class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        # Whole array is one subarray
        if k == len(nums):
            return max(nums)

        # Every element is a separate subarray
        if k == 1:
            ans = -1
            for x in nums:
                if nums.count(x) == 1:
                    ans = max(ans, x)
            return ans

        # 1 < k < len(nums)
        ans = -1

        # First element
        if nums[0] not in nums[1:]:
            ans = max(ans, nums[0])

        # Last element
        if nums[-1] not in nums[:-1]:
            ans = max(ans, nums[-1])

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna