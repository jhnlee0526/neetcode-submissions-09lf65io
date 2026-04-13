class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking with dfs recursively + visits(hashset)
        ## time : O(r * c * 4^w)
        ## space: O(w)

        visits = set() # avoid cycling
        RC, CC = len(board), len(board[0])

        def dfs(r, c, i):
            # base case
            if i == len(word):
                return True
            if (
                r not in range(RC) or
                c not in range(CC) or
                board[r][c] != word[i] or
                (r, c) in visits
            ):
                return False
            
            # add
            visits.add((r, c))  
            
            # search depth in 4 ways
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                if dfs(nextR, nextC, i + 1):
                    return True
            
            # remove
            visits.remove((r, c))
            return False


        # init dfs
        for r in range(RC):
            for c in range(CC):
                if dfs(r, c, 0):
                    return True
        return False