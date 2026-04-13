class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ## [backtracking]
        #### time : O(n² × n!) 
        #### space: O(n)
        resPerm = []        # This will hold all the generated permutations
        curPerm = []        # Temporary list for building one permutation

        def backtracking(i):
            # Base case: if we've placed all elements, add a copy of the current permutation
            if i >= len(nums):
                resPerm.append(curPerm.copy())  # Always use .copy() to avoid mutation issues
                return
            
            # Try placing nums[i] into every possible position in curPerm
            # At each level of recursion, we insert the next number at all valid positions
            for j in range(len(curPerm) + 1): 
                curPerm.insert(j, nums[i])      # Insert nums[i] at position j
                backtracking(i + 1)             # Recurse with next index
                curPerm.pop(j)                  # Backtrack: remove inserted element to restore state

        backtracking(0)      # Start the recursive process with index 0
        return resPerm       # Return all collected permutations