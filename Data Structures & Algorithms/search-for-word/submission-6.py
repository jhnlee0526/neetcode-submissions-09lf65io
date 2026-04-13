class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking with dfs recursively + paths(hashset)
        ## time : O(R × C × 4^L) 
                    # R = number of rows
                    # C = number of columns
                    # L = length of the word
        ## space: O(L)
                    # The maximum depth of the call stack is L (length of the word).

        paths = set() # avoid cycling, {(r, c), }
        RC, CC = len(board), len(board[0])
        
        def dfs(r, c, i):
            # base case
            if i == len(word):
                return True
            if (
                r not in range(RC) or
                c not in range(CC) or
                board[r][c] != word[i] or
                (r, c) in paths
            ):
                return False

            paths.add((r, c)) ## adding

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                if dfs(nextR, nextC, i + 1):
                    return True

            paths.remove((r, c)) ## removing
            return False

        # init dfs
        for r in range(RC):
            for c in range(CC):
                if dfs(r, c, 0):
                    return True
        return False
