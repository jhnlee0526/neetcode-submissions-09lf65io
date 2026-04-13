class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # DFS recursively + backtracking
        #   Time : O(n * 2^n)
        #       - Each of the n elements has 2 choices: add or remove
        #       - This branching creates 2^n possible subsets
        #       - Copying each subset into res costs O(n)
        #       - Total work = O(n * 2^n)
        #   Space: O(n) auxiliary (recursion stack)
        #       - O(n * 2^n) total including output

        res = []
        subset = []

        def dfs(i):
            # base case
            if i > len(nums) - 1:
                res.append(subset[:])   # O(n) time : copying
                return

            # backtracking
            subset.append(nums[i])  # add
            dfs(i + 1)  # O(2^n) time
            subset.pop()            # remove
            dfs(i + 1)  # O(2^n) time

            return res

        return dfs(0)
