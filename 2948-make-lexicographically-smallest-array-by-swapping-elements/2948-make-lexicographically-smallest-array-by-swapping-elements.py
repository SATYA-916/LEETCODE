class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        arr = sorted((num, i) for i, num in enumerate(nums))

        ans = nums[:]

        start = 0

        for i in range(1, len(arr) + 1):

            if i == len(arr) or arr[i][0] - arr[i - 1][0] > limit:

                group = arr[start:i]

                values = sorted(x[0] for x in group)
                indices = sorted(x[1] for x in group)

                for index, value in zip(indices, values):
                    ans[index] = value

                start = i

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna