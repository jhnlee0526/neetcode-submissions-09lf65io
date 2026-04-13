class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking (recursively)
        #### time : O(n² × n!) 
        #### space: O(n)
        res = []
        curNums = []

        def backtracking(i):
            # base case
            if i >= len(nums):
                res.append(curNums[:])
                return
            
            # len(n) + 1 : insert/remove at index 0, index2, and index3
            for j in range(len(curNums) + 1):
                curNums.insert(j, nums[i])
                backtracking(i + 1)
                curNums.pop(j)

        backtracking(0)
        return res