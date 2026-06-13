class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        j=0
        r=""
        temp=0
        for i in words:
            for k in i:
                temp=temp+weights[ord(k)-ord('a')]
                j=j+1
            r=r+chr(abs(temp%26-26)+ord('a')-1)
            temp=0
        return r



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna