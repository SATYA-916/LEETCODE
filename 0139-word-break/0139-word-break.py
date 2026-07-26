class Solution:
    def wordBreak(self, s: str, w: List[str]) -> bool:
        @cache
        def help(x):
            if x == s:
                return True
            if not s.startswith(x):
                return False
            for word in w:
                if help(x + word):
                    return True
            return False
        return help("")

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna