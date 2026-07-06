class Solution:
    def matrixScore(self, grid: List[List[int]]):

        def flip(x):
            for i in range(len(x)):
                if x[i] == 0:
                    x[i] = 1
                else:
                    x[i] = 0
            return x

        # Flip rows
        for i in range(len(grid)):
            if grid[i][0] == 0:
                grid[i] = flip(grid[i])

        # Flip columns
        for j in range(1, len(grid[0])):
            zero = 0
            one = 0

            for i in range(len(grid)):
                if grid[i][j] == 0:
                    zero += 1
                else:
                    one += 1

            if zero > one:
                for i in range(len(grid)):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0

        ans = 0
        for row in grid:
            ans += int("".join(map(str, row)), 2)

        return ans