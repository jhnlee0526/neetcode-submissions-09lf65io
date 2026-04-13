class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 🔁 Backtracking using SWAP with dfs recursively (in-place)
        ## Time : O(n!) → n factorial permutations
        ## Space: O(n) → recursion stack (excluding output)

        res = []  # To store all generated permutations

        def dfs(i):
            # ✅ Base case: reached end of list → one full permutation
            if i == len(nums):
                res.append(nums[:])  # Copy of current arrangement
                return

            # 🔄 Try placing each number at the 'i'/start position 
            for j in range(i, len(nums)):
                # 🎯 Swap: move nums[j] to the current 'i' position
                nums[i], nums[j] = nums[j], nums[i]

                # 🧗 Recursively fill the next position
                dfs(i + 1)

                # ↩️ Backtrack: undo the swap to try next possibility
                nums[i], nums[j] = nums[j], nums[i]

        dfs(0)
        return res


        # Backtracking with DFS recursively
        ## time : O(n × n!) **
        '''
            n!- permutations
            O(n)- time per permutation for insert/pop
        '''
        ## space: O(n) if 'res' is not included. Otherwise O(n x n!) because that’s how many full permutations you're storing.

        res = []
        curPerm = []
        
        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(curPerm[:])
                return
            
            for j in range(len(curPerm) + 1): # front + mid + *back
                # backtracking
                curPerm.insert(j, nums[i]) # add
                dfs(i + 1)                 # searching depth
                curPerm.pop(j)             # remove
            
        dfs(0)
        return res