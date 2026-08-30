class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        l=nums.index(max(nums))
        r=nums.index(min(nums))
        if len(nums)==1:
            return 1
        if l<len(nums)//2 and r<len(nums)//2:
            return max(l,r)+1
        elif l>=len(nums)//2 and r>=len(nums)//2: 
            return len(nums)-min(l,r)
        return min((min(l,r)+1 #left side
                    + len(nums)-max(l,r)) #right side
                    ,(max(l,r)+1),(len(nums)-min(l,r)))



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna