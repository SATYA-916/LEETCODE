class Solution:
    def pathsWithMaxScore(self, bo: List[str]) -> List[int]:
        b=[]
        for i in bo:
            b.append(list(i)[::-1])
        b=b[::-1]

        n=len(b)
        dp=[[-1]*n for _ in range(n)]
        cnt=[[0]*n for _ in range(n)]

        dp[0][0]=0
        cnt[0][0]=1

        for i in range(n):
            for j in range(n):
                if dp[i][j]==-1 or b[i][j]=='X':
                    continue

                for ni,nj in ((i+1,j),(i,j+1),(i+1,j+1)):
                    if ni<n and nj<n and b[ni][nj]!='X':
                        val=0 if b[ni][nj] in ('S','E') else int(b[ni][nj])
                        ns=dp[i][j]+val

                        if ns>dp[ni][nj]:
                            dp[ni][nj]=ns
                            cnt[ni][nj]=cnt[i][j]
                        elif ns==dp[ni][nj]:
                            cnt[ni][nj]=(cnt[ni][nj]+cnt[i][j])%(10**9+7)

        if dp[n-1][n-1]==-1:
            return [0,0]
        return [dp[n-1][n-1],cnt[n-1][n-1]]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna