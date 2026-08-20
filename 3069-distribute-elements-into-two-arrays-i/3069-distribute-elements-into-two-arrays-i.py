class Solution:
    def resultArray(self, n: List[int]) -> List[int]:
        a1=[n[0]]
        a2=[n[1]]
        for i in range(2,len(n)):
            if a1[-1]>a2[-1]:
                a1.append(n[i])
            else:
                a2.append(n[i])
        return a1+a2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna