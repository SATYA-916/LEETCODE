class Solution:
    def smallestPalindrome(self, s: str) -> str:
        print(chr(97),ord('a'))
        a,ans,k,st=[0]*26,"",0,''
        for i in s:
            a[ord(i)-ord('a')]+=1
        for i in range(26):
            if a[i]%2==1:
                st=chr(ord('a')+i)
                a[i]-=1
        for i in range(26):
            a[i]/=2
        for i in range(26):
            if a[i]>0:
                ans=ans+(chr(ord('a')+i))*int(a[i])
                a[i]=0
        return ans+st+ans[::-1]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna