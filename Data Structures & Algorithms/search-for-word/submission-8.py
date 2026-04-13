class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking, dfs recursively + hashset for visits
        ## time : O(r*c * 4^w)
        ## space: O(w)

        visits = set()
        RC, CC = len(board), len(board[0])

        def dfs(r, c, i):   # recursion
            # base case
            if i == len(word):
                return True
            if (
                r not in range(RC) or
                c not in range(CC) or
                (r, c) in visits or
                board[r][c] != word[i]
            ):
                return False
            
            # add
            visits.add((r, c))
            
            # search
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                if dfs(nextR, nextC, i + 1):
                    return True

            # remove
            visits.remove((r, c))

            return False

        
        # calling dfs initially
        for r in range(RC):
            for c in range(CC):
                if dfs(r, c, 0):
                    return True
        
        return False