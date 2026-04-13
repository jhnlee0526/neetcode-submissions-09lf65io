class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #   DFS recursively + backtracking
        #   Time : O(2^n * n)
        #       - n = number of candidates
        #       - Each candidate has 2 choices: include or skip → 2^n subsets explored
        #       - Copying each valid combination costs O(n)
        #       - Overall exponential in n
        #   Space: O(n) recursion stack (auxiliary)
        #          O(#solutions * n) total including output storage

        res = []
        comb = []
        self.sum = 0

        candidates.sort()   # sort to handle duplicates

        def dfs(i):
            # base cases
            if self.sum == target:
                res.append(comb[:])     # O(n) time: copying
                return
            if self.sum > target or i > len(candidates) - 1:
                return
            
            for j in range(i, len(candidates)):
                # skip duplicates at the same depth
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if self.sum + candidates[j] > target:
                    break

                # backtracking
                comb.append(candidates[j])    # add
                self.sum += candidates[j]
                dfs(j + 1)  # O(2^n) time

                comb.pop()                    # remove
                self.sum -= candidates[j]

            return res
        
        return dfs(0)