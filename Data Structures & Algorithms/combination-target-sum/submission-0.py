class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # [Backtracking] to find all combinations that sum to target
        ## Time : O(2^t * n) in worst case (t = target, n = len(nums))
        ## Space: O(t) for the recursion stack and current combination

        res = []   # Final list of valid combinations
        cur = []   # Current combination we're building
        total = 0  # Current sum of elements in 'cur'

        def dfs(i):
            nonlocal total

            # ✅ Base case: valid combination
            if total == target:
                res.append(cur.copy())
                return

            # ❌ Base case: out of bounds or sum too big
            if i >= len(nums) or total > target:
                return

            # 🔁 Choose current number
            cur.append(nums[i])
            total += nums[i]

            # Recurse with the same index since we can reuse the number
            dfs(i)

            # 🧹 Backtrack: remove last added number
            total -= nums[i]
            cur.pop()

            # 🔁 Move to next index (skip current number)
            dfs(i + 1)

        dfs(0)
        return res
