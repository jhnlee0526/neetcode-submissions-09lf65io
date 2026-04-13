class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS(iterative) : time O(r*c), space. O(r*c)

        # if the grid is empty or the row in the grid is empty: retur "0 island"
        # create variable "cnt" with 0 for counting islands
        # create a set to check a visited island
        # create variables "RC" "CC" for each length of rows and col
        
        # create a helper for the "breadth first search", iterative -> bfs(r, c)
            # create queue
            # add the current spot (r, c) in the queue
            # add the current spot (r, c) in visits

            # run a loop until queue is empty:
                # popleft() from the queue, and get r, c
                # check four directions from the (r, c)
                    # if r + dr in range(RC) AND
                    # c + dc in range(CC) AND
                    # (r + dr, c + dc) not in visits AND
                    # grid[r + dr][c + dc] == "1"
                        # add it to the queue
                        # add it to the visits

        # run nested loop with rows and cols, to check the each spot to initiate the helper "bfs"
            # increase "cnt" by 1
            # bfs(r, c)

        # return "cnt"

        if not grid or not grid[0]:
            return 0
        
        cnt = 0
        visits = set()
        RC, CC = len(grid), len(grid[0])

        # helper "bfs(r, c)" with queue
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visits.add((r, c))
            
            while len(queue) > 0:
                r, c = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    if (
                        r + dr in range(RC) and
                        c + dc in range(CC) and
                        (r + dr, c + dc) not in visits and
                        grid[r + dr][c + dc] == "1"
                    ):
                        queue.append((r + dr, c + dc))
                        visits.add((r + dr, c + dc))


        # initiate the helper
        for r in range(RC):
            for c in range(CC):
                if (r, c) not in visits and grid[r][c] == "1":
                    cnt += 1
                    bfs(r, c)

        return cnt