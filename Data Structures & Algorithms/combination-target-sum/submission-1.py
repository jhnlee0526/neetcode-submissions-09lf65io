class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # backtracking with dfs recursively
        res = []
        curStack = []
        sum = 0

        def dfs(i):
            nonlocal sum

            # base case
            if sum == target:
                res.append(curStack[:])
                return
            if i >= len(nums) or sum > target:
                return
            
            curNum = nums[i]
            # backtracking
            sum += curNum           # add
            curStack.append(curNum)
            dfs(i) ##               # Recurse with the SAME index since we can RE-USE the number
            sum -= curNum           # remove
            curStack.pop()

            dfs(i + 1) ##           # now move onto the next

        dfs(0)
        return res
