class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # bfs iteratively with queue
        #   time : O(r * c)
        #   space: O(r * c)
        
        if not board or not board[0]:   # edge case
            return

        RC, CC = len(board), len(board[0])
        q = deque()

        # Enqueue all the 'O' at the boarders
        for r in range(RC):
            for c in range(CC):
                if (
                    (r == 0 or r == RC - 1 or c == 0 or c == CC - 1) and   #
                    board[r][c] == 'O'                                     #
                ): 
                    q.append((r, c))
        
        # bfs with queue : '0' at the boarders -> 'T'
        while q:
            qr, qc = q.popleft()
            if board[qr][qc] == 'O':
                board[qr][qc] = 'T'

            directions = [[1, 0], [-1, 0],[0, 1], [0, -1]]
            for dr, dc in directions:
                nextR, nextC = qr + dr, qc + dc
                if (
                    nextR in range(RC) and
                    nextC in range(CC) and
                    board[nextR][nextC] == 'O'
                ):
                    q.append((nextR, nextC))

        # visit every cells to flip 'O' -> 'X', 'T' -> 'O'
        for r in range(RC):
            for c in range(CC):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'

                    