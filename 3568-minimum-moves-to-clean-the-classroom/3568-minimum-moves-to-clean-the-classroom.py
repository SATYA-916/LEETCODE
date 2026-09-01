from typing import List
from collections import deque

class Solution:

    def minMoves(self, c: List[str], energy: int) -> int:

        grid = [list(x) for x in c]

        m = len(grid)
        n = len(grid[0])

        sr = sc = 0
        litter = {}

        k = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 'S':
                    sr, sc = i, j

                elif grid[i][j] == 'L':
                    litter[(i, j)] = k
                    k += 1

        if k == 0:
            return 0

        target = (1 << k) - 1

        # visited[r][c][mask] = maximum energy reached
        visited = [
            [
                [-1] * (1 << k)
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        q = deque()

        q.append((sr, sc, energy, 0, 0))
        visited[sr][sc][0] = energy

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:

            r, col, e, mask, moves = q.popleft()

            if mask == target:
                return moves

            for dr, dc in directions:

                nr = r + dr
                nc = col + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if grid[nr][nc] == 'X':
                    continue

                if e == 0:
                    continue

                ne = e - 1
                nmask = mask

                if grid[nr][nc] == 'L':
                    bit = litter[(nr, nc)]
                    nmask = mask | (1 << bit)

                if grid[nr][nc] == 'R':
                    ne = energy

                # Same position + same litter collected
                # with more energy already seen => skip
                if visited[nr][nc][nmask] >= ne:
                    continue

                visited[nr][nc][nmask] = ne

                q.append((nr, nc, ne, nmask, moves + 1))

        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna