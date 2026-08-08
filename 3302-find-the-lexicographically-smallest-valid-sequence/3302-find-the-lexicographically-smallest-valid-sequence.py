from bisect import bisect_right

class Solution(object):
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        mp = {}

        for i, ch in enumerate(word1):
            if ch not in mp:
                mp[ch] = []
            mp[ch].append(i)

        pre = [-1] * m
        j = 0

        for i in range(n):
            if j < m and word1[i] == word2[j]:
                pre[j] = i
                j += 1

        suf = [-1] * m
        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suf[j] = i
                j -= 1

        for i in range(m):

            if i == 0:
                prev = -1
            else:
                prev = pre[i - 1]

                if prev == -1:
                    break

            candidate = prev + 1

            if candidate >= n:
                break

            if word1[candidate] == word2[i]:
                continue

            if i < m - 1:
                if suf[i + 1] == -1:
                    continue

                if suf[i + 1] <= candidate:
                    continue

            ans = pre[:i]
            ans.append(candidate)

            prev = candidate

            for k in range(i + 1, m):
                arr = mp.get(word2[k], [])

                pos = bisect_right(arr, prev)

                if pos == len(arr):
                    ans = []
                    break

                nxt = arr[pos]
                ans.append(nxt)
                prev = nxt

            if len(ans) == m:
                return ans

        # If mismatch was never useful, exact sequence may be valid
        if pre[-1] != -1:
            return pre

        return []

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna