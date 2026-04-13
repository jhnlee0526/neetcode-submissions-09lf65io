class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # DFS recursively for backtracking (add / remove)
        #   time : O(2ᵗ * n) : 
        #       1.You explore up to O(2ᵗ) paths. (backtracking recursively)
        #       2.For each valid path, you COPY a list that can be up to O(n) long.
        #   space: O(t) : max depth of recursion stack and curNums list

        self.res = []
        self.curNums = []
        self.sum = 0

        def dfs(i): # index
            # base cases
            if self.sum == target:
                self.res.append(self.curNums[:]) ## O(n) time - need to use the copy
                return
            if i > len(nums) - 1 or self.sum > target:
                return

            cur = nums[i]
            
            # BACKTRACKING (ADD / REMOVE)
            self.sum += cur         # ADD
            self.curNums.append(cur)
            dfs(i)                  ## O(2ᵗ) time — recursive branching: include current number (can re-use the same number)
            
            self.sum -= cur         # REMOVE
            self.curNums.pop()
            dfs(i + 1)              ## O(2ᵗ) time — recursive branching: skip current number

        dfs(0) # starting at index 0
        return self.res