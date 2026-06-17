class Solution:
    def reverseWords(self, s: str) -> str:
        ans=s.strip()
        x=""
        for i in ans.split()[::-1]:
            x=x+" "+i
        return x[1:]
