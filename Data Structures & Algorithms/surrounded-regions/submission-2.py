class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # dfs recursively
        #   time : O(r * c)
        #   space: O(r * c)
        '''
            1. (DFS) Capture unsurrounded regions (O -> T)
            2. Capture surrounded regions (O -> X)
            3. Uncapture unsurrounded regions (T -> O)
        '''

        RC, CC = len(board), len(board[0])

        # 1. (DFS) Capture unsurrounded regions (O -> T)
        def dfs(r, c): # recursively
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                board[r][c] != 'O'
            ):
                return
            
            board[r][c] = 'T'

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                dfs(nextR, nextC)
        
        # vertical boarders
        for r in range(RC):
            if board[r][0] == 'O':      # left boarder
                dfs(r, 0)
            if board[r][CC - 1] == 'O': # right boarder
                dfs(r, CC - 1)

        # horizontal boarders
        for c in range(CC):
            if board[0][c] == 'O':      # top boarder
                dfs(0, c)
            if board[RC - 1][c] == 'O': # bottom boarder
                dfs(RC - 1, c)


        # 2. Flip all truly surrounded 'O's → 'X', and restore 'T' → 'O'
        for r in range(RC):
            for c in range(CC):
                if board[r][c] == 'O':  # Capture surrounded regions (O -> X)
                    board[r][c] = 'X'
                if board[r][c] == 'T':  # Uncapture unsurrounded regions (T -> O)
                    board[r][c] = 'O'
