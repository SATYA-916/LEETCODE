class Solution:
    def reverseParentheses(self, s: str) -> str:
        o,re=[],[]
        for i in range(len(s)):
            if s[i]=='(':
                o.append(i)
            if s[i]==')':
                re.append([o.pop(),i])
        for i in re:
            print(s[:i[0]],s[i[1]:i[0]:-1],s[i[1]:])
            s=s[:i[0]]+s[i[1]:i[0]:-1]+s[i[1]:]
        re=""
        for i in s:
            if i not in " ()":
                re+=i
        return re


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna