class Solution:
    def processStr(self, s: str, k: int) -> str:
        st=[]
        for i in s:
            if i.isalpha():
                st.append(i)
            if i=='#':
                ans=st.copy()
                for i in st:
                    ans.append(i)
                st=ans
            if i=='%':
                ans=[]
                while(st):
                    ans.append(st.pop())
                st=ans
            if i=="*":
                st.pop()
        if k>=len(st):
            return "."
        return st[k]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna