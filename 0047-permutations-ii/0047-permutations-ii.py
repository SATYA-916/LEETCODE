class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nu=[False]*len(nums)
        res=set()
        def help(ans,nu):
            if len(ans)==len(nums):
                res.add(tuple(ans))
                return
            for i in range(len(nums)):
                if not nu[i]:
                    nu[i]=True
                    help(ans+[nums[i]],nu)
                    nu[i]=False
            return res
        x=help([],nu)
        ans=[]
        for i in x:
            ans.append(list(i))
        return ans

                    
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna