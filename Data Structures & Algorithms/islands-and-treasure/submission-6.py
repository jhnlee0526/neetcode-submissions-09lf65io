class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs(from multiple-source) iteratively with queue + hashset for visits
        #   time : O(R * C), Each cell is updated at most once.
        #   space: O(R * C), queue

        if not grid or not grid[0]:     # edge case
            return

        RC, CC = len(grid), len(grid[0])
        q = deque()
        visits = set()

        # Enqueue all treasure cells (value 0)
        for r in range(RC):
            for c in range(CC):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visits.add((r, c))

        def bfs():                      # iteratively with queue
            distance = 0
                 
            while q:
                for _ in range(len(q)):
                    qr, qc = q.popleft()
                    # mark this cell with its distance to nearest treasure
                    grid[qr][qc] = distance

                    # explore neighbors
                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for dr, dc in directions:
                        nextR, nextC = qr + dr, qc + dc
                        if (
                            nextR in range(RC) and 
                            nextC in range(CC) and
                            (nextR, nextC) not in visits and
                            grid[nextR][nextC] != -1    # skip a wall
                        ):
                            visits.add((nextR, nextC))
                            q.append((nextR, nextC))
                distance += 1

        # 4) Invoke BFS to fill the grid
        bfs()
                 


