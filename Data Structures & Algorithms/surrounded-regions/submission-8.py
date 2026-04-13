class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # dfs recursively
        #   time :
        #   space:
        
        # edge case
        if not board or not board[0]:
            return

        RC, CC = len(board), len(board[0])
        visits = set()  # {(r, c), ..}
        
        def dfs(r, c):  # recursively 'O' -> 'T'
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
                if (
                    nextR in range(RC) and
                    nextC in range(CC) and
                    board[nextR][nextC] == 'O'
                ):
                    dfs(nextR, nextC)


        # check the border 'O' -> 'T'
        for r in range(RC): # left and right
            dfs(r, 0)
            dfs(r, CC - 1)
        
        for c in range(CC): # top and bottom
            dfs(0, c)
            dfs(RC - 1, c)
      
        # traverse the board:'O' -> 'X', 'T' -> 'O'
        for r in range(RC):
            for c in range(CC):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'