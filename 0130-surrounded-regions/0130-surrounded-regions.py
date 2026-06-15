class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) <= 1:
            return

        def chk(i, j):
            d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for a, b in d:
                ni = i + a
                nj = j + b

                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] == "O":
                    board[ni][nj] = "@"
                    chk(ni, nj)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                    if board[i][j] == "O":
                        board[i][j] = "@"
                        chk(i, j)

        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "@":
                    board[i][j] = "O"

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna