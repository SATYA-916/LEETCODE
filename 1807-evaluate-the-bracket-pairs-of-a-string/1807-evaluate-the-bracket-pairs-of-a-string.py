class Solution:
    def evaluate(self, st: str, knowledge: list[list[str]]) -> str:
        
        d,ans,res,s={},"","",0
        for i in knowledge:
            d[i[0]]=i[1]
        for i in st:
            if i=='(':
                s=1
                continue
            if i==')':
                s=0
                if ans in d:
                    res+=d[ans]
                else:
                    res+='?'
                ans=""
                continue
            if s:
                ans+=i
            else:
                res+=i
        # If you are struggling with the nested bracket logic, check the "Video Solutions" 
        # section in the Solutions tab on the left pane of your editor!
        print(res)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna