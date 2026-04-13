class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # [Backtracking] with DFS recursively + hashset for visits
        #   Time  : O(RC · 4^L), where L = len(word), RC = board size
        #   Space : O(L) for recursion stack + O(RC) for visited set
    
        RC, CC = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visits = set()  # {(r, c), ..}

        def dfs(r, c, i):
            # base case#1: out of bounds, visited, mismatch
            if (
                r not in range(RC) or
                c not in range(CC) or
                (r, c) in visits or
                board[r][c] != word[i]
            ): 
                return False
            # base case#2: reached end of word — match found!
            if i == len(word) - 1:
                return True

            # backtracking
            visits.add((r, c))  # add
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i + 1):
                    return True
            visits.remove((r, c)) # remove
            return False

        for r in range(RC):
            for c in range(CC):
                if dfs(r, c, 0):
                    return True
        
        return False