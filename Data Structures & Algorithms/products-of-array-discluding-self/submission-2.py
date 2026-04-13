class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## brute-force solution
        #### time : 0(n)
        #### space: O(n)
        # reverseNums = nums[::-1] #reverse list
        # res = []
        # n = len(nums)
        # for i in range(n):
        #     product = 1
        #     for j in range(len(reverseNums)):
        #         # match index from original
        #         orig_j = n - 1 - j
        #         if i != orig_j:
        #             product *= reverseNums[j]
        #     res.append(product)
        # return res
        
        
        ## "Prefix and Suffix Product" algorithm
        #### time : O(n)
        #### space: O(n)
        n = len(nums) # n = 4... [1, 2, 4, 6]
        res = [1] * n # [1, 1, 1, 1]

        # Step 2: Calculate prefix products (products to the left)
        prefix = 1
        for i in range(n): #0, 1, 2, 3
            res[i] = prefix
            prefix *= nums[i]
        # res = [1, 1, 2, 8]

        # Step 3: Calculate suffix products (products to the right) and multiply
        suffix = 1
        for i in range(n - 1, -1, -1): #3, 2, 1, 0
            res[i] *= suffix
            suffix *= nums[i]
        # res = [48, 24, 12, 8]
        
        return res
