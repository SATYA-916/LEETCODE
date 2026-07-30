from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        x,k,m,pre,ans=list(word),2,1,{},0
        d = Counter(x)
        x = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        d={2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
        for i in x:
            d[k].append(i)
            k+=1
            if k>9:
                k=2
        for i in d:
            t=1
            for j in d[i]:
                pre[j]=t
                t+=1
        for i in word:
            ans+=pre[i]
        return ans
            
             




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna