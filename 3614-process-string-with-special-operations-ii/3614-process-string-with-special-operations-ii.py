class Solution:
    def processStr(self, s: str, k: int) -> str:
        ans = 0

        for i in s:
            if i.isalpha():
                ans += 1
            elif i == '#':
                ans *= 2
            elif i == '%':
                pass
            elif i == '*' and ans > 0:
                ans -= 1

        if k >= ans:
            return "."

        for i in s[::-1]:
            if i.isalpha():
                if k == ans - 1:
                    return i
                ans -= 1

            elif i == '#':
                ans //= 2
                k %= ans

            elif i == '%':
                k = ans - 1 - k

            elif i == '*':
                ans += 1

        return "."