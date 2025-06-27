# Time Complexity : O(n!), trying every possible queen position per row
# Space Complexity : O(n^2), to store board configurations
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach: Backtracking with column and diagonal conflict checks

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        cols, pos_diag, neg_diag = set(), set(), set()

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                board[r][c] = "Q"
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                backtrack(r + 1)

                board[r][c] = "."
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        backtrack(0)
        return res
