class Solution:
    def targetIndices(self, arr: List[int], t: int) -> List[int]:
        arr.sort()
        ans=[]
        for i in range(len(arr)):
            if arr[i]==t:
                ans.append(i)
        return ans

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna