class Solution:
    def longestPrefix(self, s: str) -> str:
        se=set()
        m=""
        for i in range(len(s)):
            if s[:i]==s[-i:]:
                m=s[:i]
        return m
        