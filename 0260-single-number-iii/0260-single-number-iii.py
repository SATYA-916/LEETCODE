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