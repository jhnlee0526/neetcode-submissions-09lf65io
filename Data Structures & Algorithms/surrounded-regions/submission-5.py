class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # dfs recursively
        #   time : O(r * c)
        #   space: O(r * c)
        '''
        1. Using dfs, 'O' at the boaders -> 'T' (temporarily)
        2. Visit each cells, 'O' inside -> 'X' & 'T' at the boarder -> 'O'
        '''
        RC, CC = len(board), len(board[0])

        def dfs(r, c): # recursively : 'O' at the boarders -> 'T'
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                board[r][c] != 'O'
            ):
                return
            
            board[r][c] = 'T'
            directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                if (
                    nextR in range(RC) and
                    nextC in range(CC) and 
                    board[nextR][nextC] == 'O'
                ):
                    dfs(nextR, nextC)
        
        # left and right boarders
        for r in range(RC):
            if board[r][0] == 'O':       # left
                dfs(r, 0)
            if board[r][CC - 1] == 'O':  # right
                dfs(r, CC - 1)
        
        # top and bottom boarders
        for c in range(CC):
            if board[0][c] == 'O':       # top
                dfs(0, c)
            if board[RC - 1][c] == 'O':  # bottom
                dfs(RC - 1, c)
        
        # traverse each cells to flip 'O' -> 'X', and to return 'T' -> 'O'
        for r in range(RC):
            for c in range(CC):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'


