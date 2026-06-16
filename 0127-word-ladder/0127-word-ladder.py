class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def valid(l,x):
            ans=set()
            for i in l:
                c=0
                for j in range(len(x)):
                    if i[j]!=x[j]:
                        c+=1
                if c==1:
                    ans.add(i)
            return ans
        def dfs(s,y,step,k): 
            if y==endWord:
                return step
            if s==None:
                return float('inf')
            l=valid(s,y)#choice
            for i in l:
                s.remove(i)
                k=min(dfs(s,i,step+1,k),k)
                s.add(i)#backtrack
            return k
        s,k=set(),101
        for i in wordList:
            s.add(i)
        if endWord not in wordList:
            return 0
        k=dfs(s,beginWord,0,k)
        return 0 if k==101 else k+1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna