class Solution:
    def binaryGap(self, n: int) -> int:
        x = bin(n)[2:]

        ans = 0

        for i in range(len(x)):
            if x[i] == '1':
                j = i + 1
                while j < len(x) and x[j] != '1':
                    j += 1

                if j < len(x):
                    ans = max(ans, j - i)

        return ans