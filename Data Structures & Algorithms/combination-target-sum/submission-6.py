class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Backtracking : bfs recursively
        #   time : O(2^n) worst case - exponential branching (add/remove)
        #   space: O(2^n) for recursive stack & result list

        res = []
        comb = []
        self.sum = 0

        def dfs(i): # index
            # base case
            if self.sum == target:
                res.append(comb[:]) # copy the comb list: O(n) time
                return
            if (
                self.sum > target or 
                i > len(nums) - 1
            ):
                return
            
            # backtracking
            # add
            comb.append(nums[i])
            self.sum += nums[i]
            dfs(i)  # continue with the same index b/c allows re-use
            # remove
            comb.pop()
            self.sum -= nums[i]
            dfs(i + 1)  # move to the next index to skip current number

            return res

        return dfs(0)
