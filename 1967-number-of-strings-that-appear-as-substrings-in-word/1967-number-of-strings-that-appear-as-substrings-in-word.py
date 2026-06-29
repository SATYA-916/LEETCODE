class Solution:
    def numOfStrings(self, p: List[str], w: str) -> int:
        c=0
        for i in p:
            if i in w:
                c+=1
        return c


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna