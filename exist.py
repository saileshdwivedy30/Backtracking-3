# Time Complexity : O(m * n * 4^len(word)), worst case DFS from every cell
# Space Complexity : O(len(word)), recursion stack
# Did this code successfully run on Leetcode : Yes

# Approach: Backtracking using DFS

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                word[i] != board[r][c] or (r, c) in visited):
                return False

            visited.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            visited.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False
