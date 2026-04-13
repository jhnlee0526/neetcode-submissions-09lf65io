class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS recursively for backtracking (add / remove), using hashset for visits
        #   time : O(4^w * r*c) - w = len(word), r = rows, c = cols
        #           four ways to backtracking + checking every cells
        #   space: O(w) - the recursion stack + visits set

        visits = set()  # [(r, c), ..]
        RC, CC = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def dfs(r, c, i):   # i : word count
            # base cases
            if i == len(word): ## we’ve matched the whole word
                return True
            if (
                r not in range(RC) or
                c not in range(CC) or
                (r, c) in visits or
                board[r][c] != word[i]
            ):
                return False
            
            # backtracking (add / remove)
            visits.add((r, c))      # ADD
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                if dfs(nextR, nextC, i + 1):
                    return True
            
            visits.remove((r, c))   # REMOVE

            return False        

        # initally calling dfs()
        for r in range(RC):
            for c in range(CC):
                if dfs(r, c, 0):
                    return True
        
        return False