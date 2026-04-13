class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # DFS recursively + bactracking
        #   Time : O(N^(T/M)) in worst case
        #       - N = number of candidates
        #       - T = target value
        #       - M = minimum candidate value
        #       1. Each recursive call branches into up to N choices (not just 2): remove, add once, add twice ...
        #       2. Recursion depth can be as large as T/M (keep adding smallest number).
        #       3. Copying each valid combination costs O(k), where k ≤ T/M.
        #       - Overall exponential, but tighter bound than O(2^T * n).
        #   Space: O(T/M) auxiliary (recursion stack + curNums list)
        #          O(#solutions * k) total including output

        res = []
        comb = []
        self.sum = 0

        def dfs(i):
            # base cases
            if self.sum == target:
                res.append(comb[:]) # O(k) time : copying
                return
            if self.sum > target or i > len(nums) - 1:
                return
            
            # backtracking
            comb.append(nums[i])    # add
            self.sum += nums[i]
            dfs(i)      # continue with same index → allows reuse of nums[i]
            
            comb.pop()              # remove
            self.sum -= nums[i]
            dfs(i + 1)  # move to next index → skip current number

            return res
            
        return dfs(0)