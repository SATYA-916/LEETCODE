class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        f=[0]*26
        for i in s:
            f[ord(i)-ord('a')]=f[ord(i)-ord('a')]+1
            st=f[ord(i)-ord('a')]
        for i in f:
            if i!=st and i!=0:
                print(i,st)
                return False
        return True
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna