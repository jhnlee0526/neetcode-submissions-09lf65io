class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking with DFS() 
        RC, CC = len(board), len(board[0])
        paths = set() # {(r, c), }

        def dfs(r, c, i): # backtracking recursively
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
            
            paths.add((r, c)) ##
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                if dfs(nextR, nextC, i + 1):
                    return True
            
            paths.remove((r, c)) ##

            return False
        
        # initiating dfs()
        for r in range(RC):
            for c in range(CC):
                if dfs(r, c, 0):
                    return True # if you find at least one True, it's the answer!
                
        return False