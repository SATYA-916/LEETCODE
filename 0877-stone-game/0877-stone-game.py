class Solution:
    def stoneGame(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return nums[i]
            
            pick_left = nums[i] - dfs(i+1, j)
            pick_right = nums[j] - dfs(i, j-1)
            
            return max(pick_left, pick_right)
        
        return dfs(0, len(nums)-1) >= 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna