class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            s^=i
        if s!=0:
            return len(nums)
        for i in nums:
            if i!=0:
                return len(nums)-1
        return 0
        