class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        def help(x,temp):
            nonlocal ans
            if len(x)==3:
                if x not in s:
                    s.add(x)
                    ans+=1
                    return 
                return 
            for i in range(len(digits)):
                if not (digits[i]==0 and len(x)==2) and temp[i]==0:
                    temp[i]=1
                    help(x+str(digits[i]),temp)
                    temp[i]=0

        ans=0
        s=set()
        temp=[0]*len(digits)
        for i in range(len(digits)):
            if digits[i]%2==0 :
                temp[i]=1
                help(str(digits[i]),temp)
                temp[i]=0
        print(s)
        return ans
        
            
                     
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna