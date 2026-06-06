class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lf=0
        ri=0
        ans=[]
        for i in range(1,len(nums)):
            ri+=nums[i]
        for i in range(1,len(nums)):
            ans.append(abs(lf-ri))
            lf+=nums[i-1]
            ri-=nums[i]
        ans.append(lf)
        return ans
        