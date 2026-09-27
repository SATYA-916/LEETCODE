class Solution:
    def reverseParentheses(self, s: str) -> str:
        st,ans,i=[],[],0
        while(i<len(s)):
            if s[i]==')':
                while(st[-1]!='('):
                    ans.append(st.pop())
                st.pop()
                st+=ans
                ans=[]
            else:
                st.append(s[i])
            i+=1
        return "".join(st)
                


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna