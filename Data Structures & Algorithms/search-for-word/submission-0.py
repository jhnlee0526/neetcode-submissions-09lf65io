class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # [backtracking] - "dfs()" with set() to track paths
        ## Time : O(m * n * 4^k), where m = rows, n = cols, k = len(word)
        ## Space: O(k) for the recursion stack + O(k) for the path set

        RC, CC = len(board), len(board[0])
        paths = set()  # Track the cells currently in our search path

        def dfs(r, c, i):
            # base case: we’ve matched the whole word
            if i == len(word):
                return True
            
            # out of bounds, wrong char, or already visited in this path
            if (
                r not in range(RC) or
                c not in range(CC) or
                board[r][c] != word[i] or
                (r, c) in paths
            ):
                return False

            paths.add((r, c))  # add current cell to the path

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # down, up, right, left
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                if dfs(nextR, nextC, i + 1):  # recursive search
                    return True

            paths.remove((r, c))  # backtrack if no path works out
            return False

        # Try to start DFS from each cell on the board
        for r in range(RC):
            for c in range(CC):
                if dfs(r, c, 0):
                    return True

        return False  # no path matched the word