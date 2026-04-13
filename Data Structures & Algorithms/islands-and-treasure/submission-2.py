class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs iteratively with queue + hashset for visits
        #   time : O((R × C)²)
        '''
            BFS runs      = O(R × C)
            work per BFS  = O(R × C)
            ⇒ Total time    = O((R × C) × (R × C)) = O((R × C)²)
        '''
        #   space: O(R × C), visits and queue

        RC, CC = len(grid), len(grid[0])
        INF = 2147483647

        def bfs(r, c):
            q = deque()
            q.append((r, c))       # [(r, c), ...]
            # q = deque([(r, c)])

            visited = set()        # start with an empty set
            visited.add((r, c))    # mark the source as visited
            steps = 0

            while q:
                for _ in range(len(q)):
                    qr, qc = q.popleft()
                    
                    if grid[qr][qc] == 0:
                        return steps

                    directions = [[1,0],[-1,0],[0,1],[0,-1]]
                    for dr, dc in directions:
                        nextR, nextC = qr + dr, qc + dc
                        if (
                            nextR in range(RC) and
                            nextC in range(CC) and
                            (nextR, nextC) not in visited and
                            grid[nextR][nextC] != -1
                        ):
                            visited.add((nextR, nextC))
                            q.append((nextR, nextC))

                steps += 1

            # No gate found
            return INF

        # initial invokation of bfs()
        for r in range(RC):
            for c in range(CC):
                if grid[r][c] == INF:
                    # only run this block for “unfilled” rooms
                    grid[r][c] = bfs(r, c)
        