class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        x=[]
        for i in range(len(rowShift)):
            x.append(grid[i][rowShift[i]:] +grid[i][:rowShift[i]])
        y = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                y[i][j]=x[j][i]
        x=[]
        for i in range(len(rowShift)):
            x.append(y[i][colShift[i]:] +y[i][:colShift[i]])
        y = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                y[i][j]=x[j][i]
        return y
        





        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna