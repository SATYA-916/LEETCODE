from functools import cache
class Solution:
    def countDigitOne(self, n: int) -> int:
        @cache
        def help(n, ones, bound):
            a = 0
            if n == "":
                return ones
            if not bound:  # not bounded
                for i in range(10):
                    if i == 1:
                        a += help(n[1:], ones + 1, False)
                    else:
                        a += help(n[1:], ones, False)
            else:  # bounded
                for i in range(int(n[0])):
                    if i == 1:
                        a += help(n[1:], ones + 1, False)
                    else:
                        a += help(n[1:], ones, False)
                if n[0] == '1':
                    a += help(n[1:], ones + 1, True)
                else:
                    a += help(n[1:], ones, True)
            return a
        ans = help(str(n), 0, True)
        return ans