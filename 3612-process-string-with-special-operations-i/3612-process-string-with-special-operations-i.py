class Solution:
    def processStr(self, s: str) -> str:
        ans=""
        for i in s:
            if i.isalpha():
                ans=ans+i
            if i=='#':
                ans=ans+ans
            if i=='%':
                ans=ans[::-1]
            if i=="*":
                ans=ans[:len(ans)-1]
        return ans




        