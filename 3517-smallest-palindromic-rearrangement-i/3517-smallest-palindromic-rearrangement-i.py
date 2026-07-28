class Solution:
    def smallestPalindrome(self, s: str) -> str:
        a = [0] * 26
        ans = ""
        st = ""

        for ch in s:
            a[ord(ch) - ord('a')] += 1

        for i in range(26):
            if a[i] % 2 == 1:
                st = chr(ord('a') + i)
                a[i] -= 1

        for i in range(26):
            a[i] //= 2

        for i in range(26):
            if a[i] > 0:
                ans += chr(ord('a') + i) * a[i]

        return ans + st + ans[::-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna