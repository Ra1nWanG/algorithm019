class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generate():
            board = []
            for i in range(n):
                rows[queens[i]] = "Q"
                board.append("".join(rows))
                rows[queens[i]] = "."
            return board
        
        def solve(row, cols, pie, na):
            if n == row:
                board = generate()
                res.append(board)
            else:
                bits = ((1 << n) - 1) & (~(cols | pie | na))
                while bits:
                    pos = bits & (-bits)
                    bits = bits & (bits - 1)
                    col = bin(pos - 1).count('1')
                    queens[row] = col
                    solve(row + 1, cols | pos, (pie | pos) << 1, (na | pos) >> 1)
        res = []
        rows = ["."] * n
        queens = [-1] * n
        solve(0, 0, 0, 0)
        return res
