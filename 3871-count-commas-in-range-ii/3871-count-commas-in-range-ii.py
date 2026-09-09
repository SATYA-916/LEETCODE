class Solution:
    def countCommas(self, n: int) -> int:
        if n<10**3:
            return 0
        elif n<10**6:
            return n-999
        elif n<10**9:
            return 2*(n-999_999)+999000
            #1004590=> 2[1.000.000--1004590] 1[1000--1.000.000]
        elif n<10**12:
            return 3*(n-999_999_999)+2*(999_999_999-999_999)+999000
        elif n<10**15:
            return 4*(n-999_999_999_999)+3*(999_999_999_999-999_999_999)+2*(999_999_999-999_999)+999000
        return 5*(n-999_999_999_999_999)+4*(999_999_999_999_999-999_999_999_999)+3*(999_999_999_999-999_999_999)+2*(999_999_999-999_999)+999000
        # 1.000.000               10**6
        # 1.000.000.000           10**9
        # 1.000.000.000.000       10**12
        # 1.000.000.000.000.000   10**15


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna