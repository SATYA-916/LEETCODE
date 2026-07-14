class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis=[[] for i in range(len(grid))]
        def help(i,j):
            if grid[i][j] == "0" or grid[i][j] == "@":
                return
            grid[i][j]="@"
            if i+1<len(grid):
                help(i+1,j)
            if i-1>=0:
                help(i-1,j)
            if j+1<len(grid[0]):
                help(i,j+1)
            if j-1>=0:
                help(i,j-1)
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    ans+=1
                    help(i,j)
        print(grid)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna