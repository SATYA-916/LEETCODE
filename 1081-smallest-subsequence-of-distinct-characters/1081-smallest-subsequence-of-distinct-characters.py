class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
        stack = []
        vis = set()
        for i, ch in enumerate(s):
            if ch in vis:
                continue
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                vis.remove(stack.pop())
            stack.append(ch)
            vis.add(ch)
        return "".join(stack)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna