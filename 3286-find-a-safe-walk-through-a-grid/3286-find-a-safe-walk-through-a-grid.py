class Solution:
    def findSafeWalk(self, grid: List[List[int]], h: int) -> bool:
        n, m = len(grid), len(grid[0])

        best = [[-1] * m for _ in range(n)]

        def help(x, y, h):
            h -= grid[x][y]

            if h < 1:
                return -1

            if x == n - 1 and y == m - 1:
                return h

            if best[x][y] >= h:
                return -1
            best[x][y] = h

            ans = -1

            dire = [[1,0],[0,1],[-1,0],[0,-1]]

            for dx, dy in dire:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    ans = max(ans, help(nx, ny, h))

            return ans

        return help(0, 0, h) >= 1