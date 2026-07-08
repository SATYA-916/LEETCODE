class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # prefix sum of non-zero digits
        preSum = [0] * (n + 1)

        # prefix count of non-zero digits
        cnt = [0] * (n + 1)

        # prefix value formed by non-zero digits
        preVal = [0] * (n + 1)

        for i, ch in enumerate(s):
            d = int(ch)
            preSum[i + 1] = preSum[i]
            cnt[i + 1] = cnt[i]
            preVal[i + 1] = preVal[i]

            if d != 0:
                preSum[i + 1] += d
                cnt[i + 1] += 1
                preVal[i + 1] = (preVal[i] * 10 + d) % MOD

        # powers of 10
        p10 = [1] * (cnt[-1] + 1)
        for i in range(1, len(p10)):
            p10[i] = (p10[i - 1] * 10) % MOD

        ans = []

        for l, r in queries:
            sm = preSum[r + 1] - preSum[l]

            digits = cnt[r + 1] - cnt[l]

            x = (preVal[r + 1] - preVal[l] * p10[digits]) % MOD

            ans.append((x * sm) % MOD)

        return ans