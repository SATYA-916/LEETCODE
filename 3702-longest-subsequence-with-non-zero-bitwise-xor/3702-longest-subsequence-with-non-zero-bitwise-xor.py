class Solution(object):
    def longestSubsequence(self, nums):
        x=0
        nonzero=0
        for i in nums:
            x=x^i
            if i!=0:
                nonzero+=1
        if x!=0:
            return len(nums)
        elif nonzero>0:
            return len(nums)-1
        else:
            return 0
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna