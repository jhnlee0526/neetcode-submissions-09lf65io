class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS(backtracking with recursion) : time O(r*c), space O(r*c)

        # if the grid is empty or the row in the grid is empty, return "0 island"
        # create variable "cnt" with 0 for counting islands
        # create a set to check a visited island
        # created variables "RC" and "CC" for each length of rows and cols
        
        # create a helper for the "depth first search", recursion -> dfs(r, c) 
            # BASECASE:
                # 1. if r is not in the range of RC (rows length) OR
                # 2. if c is not in the range of CC (cols length) OR
                # 3. if the current spot has a value of "0" OR
                # 4. if the current spot has been visited before
                # ==> RETURN...do nothing
            # set this spot (r, c) as "visited" by adding it to the visits set
            # check four directions from the spot by invoking the helper "dfs(r, c)" recursively

        # run a loop on rows, and run another loop on cols inside of the loop, to access each row and col
            # if the current spot in the grid has value of "1" AND if the spot never been visited before:
                # increase the "cnt"
                # run helper "dfs(r, c)" to check the status of the surrounding spots
        
        # return "cnt"

        if not grid or not grid[0]:
            return 0
        
        cnt = 0
        visits = set()
        RC, CC = len(grid), len(grid[0])

        # helper for depth first search
        def dfs(r , c):
            if (
                r not in range(RC) or
                c not in range(CC) or
                (r, c) in visits or
                grid[r][c] == "0"
            ):
                return
            
            visits.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # initiating the helper
        for r in range(RC):
            for c in range(CC):
                if (r, c) not in visits and grid[r][c] == "1":
                    cnt += 1
                    dfs(r, c)

        return cnt