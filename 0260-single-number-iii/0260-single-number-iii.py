class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = 0
        for num in nums:
            ans ^= num

        bit = 1
        while (ans & bit) == 0:
            bit <<= 1

        a = b = 0
        for num in nums:
            if num & bit:
                a ^= num
            else:
                b ^= num

        return [a, b]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna