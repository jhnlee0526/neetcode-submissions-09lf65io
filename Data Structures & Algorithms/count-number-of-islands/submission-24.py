class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS iteratively + queue + hashset for visits
        #   Time: O(R × C)
        #       → Each cell is visited once at most
        #   Space: O(R × C)
        #       → HashSet for visited cells + queue in worst ca

        # edge case
        if not grid or not grid[0]:
            return 0

        cnts = 0
        q = deque()     # [(r, c), ...]
        visits = set()  # {(r, c), ...}
        
        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def bfs(r, c):
            q.append((r, c))
            visits.add((r, c))

            while q:
                qr, qc = q.popleft()
                for dr, dc in directions:
                    nextR, nextC = qr + dr, qc + dc
                    if (
                        nextR in range(RC) and
                        nextC in range(CC) and
                        grid[nextR][nextC] == '1' and
                        (nextR, nextC) not in visits
                    ):
                        q.append((nextR, nextC))
                        visits.add((nextR, nextC))
                        
        for r in range(RC):
            for c in range(CC):
                if (
                    grid[r][c] == '1' and
                    (r, c) not in visits
                ):
                    bfs(r, c)
                    cnts += 1

        return cnts