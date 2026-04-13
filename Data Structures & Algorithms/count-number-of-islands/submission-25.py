class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # ✅ BFS iteratively with queue (no helper function)
        #   Time : O(R × C) — each cell visited once
        #   Space: O(R × C) — visited set + queue in worst case

        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visits = set()
        count = 0

        for r in range(RC):
            for c in range(CC):
                if (r, c) not in visits and grid[r][c] == '1':
                    # Start BFS from this unvisited land cell
                    q = deque()
                    q.append((r, c))
                    visits.add((r, c))
                    count += 1  # Found a new island

                    while q:
                        qr, qc = q.popleft()
                        for dr, dc in directions:
                            nextR, nextC = qr + dr, qc + dc
                            if (
                                0 <= nextR < RC and
                                0 <= nextC < CC and
                                grid[nextR][nextC] == '1' and
                                (nextR, nextC) not in visits
                            ):
                                q.append((nextR, nextC))
                                visits.add((nextR, nextC))

        return count