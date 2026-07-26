class Solution:
    def maximumProduct(self, n: List[int]) -> int:
        n1,n2,n3,m1,m2=float('-inf'),float('-inf'),float('-inf'),float('inf'),float('inf')
        for i in n:
            if i>n1:
                n3=n2
                n2=n1
                n1=i
            elif i>n2:
                n3=n2
                n2=i
            elif i>n3:
                n3=i
            if i<m1:
                m2=m1
                m1=i
            elif i<m2:
                m2=i
        print(n1,n2,n3,m1,m2)
        return max(n1*n2*n3,n1*m1*m2)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna