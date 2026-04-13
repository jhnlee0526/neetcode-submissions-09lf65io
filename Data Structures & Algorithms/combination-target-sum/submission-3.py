class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # BFS iteratively w/ queue (NO backtracking)
        #   Time  : O(2^n) worst case — exponential branching
        #   Space : O(2^n) for queue and result storage

        # edge case
        if not nums:
            return []

        res = []

        def bfs(i):
            q = deque([([], 0, i)])  # [(comboSoFar, sumSoFar, indexToStartFrom)]
            while q:
                qCombo, qTotal, qIdx = q.popleft()
                if qTotal == target:
                    res.append(qCombo)
                    continue
                if qTotal > target:
                    continue

                for i in range(qIdx, len(nums)): # can re-use nums[qIdx]
                    num = nums[i]
                    q.append((qCombo + [num], qTotal + num, i))  # reuse same number

        bfs(0)
        return res

        
        # [preferred] Backtracking with DFS recursively
        #   time : O(2ᵗ * n) : 
        #       1.You explore up to O(2ᵗ) paths. (backtracking recursively)
        #       2.For each valid path, you COPY a list that can be up to O(n) long.
        #   space: O(t) : max depth of recursion stack and curNums list
        
        res = []
        curNums = []
        self.sum = 0

        def dfs(i):
            # base cases
            if (
                i > len(nums) - 1 or
                self.sum > target
            ):
                return False
            if self.sum == target:
                res.append(curNums.copy())  # O(n) time : copying
                return
            
            # backtracking
            self.sum += nums[i]     # add
            curNums.append(nums[i])
            dfs(i)  ## O(2ᵗ) time, can re-use the same number

            self.sum -= nums[i]     # remove
            curNums.pop()
            dfs(i + 1)  # O(2ᵗ) time, skip the current number

        dfs(0)  # index 0
        return res