class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## brute-force solution
        #### time : 0(n)
        #### space: O(n)
        reverseNums = nums[::-1] #reverse list
        res = []
        n = len(nums)
        for i in range(n):
            product = 1
            for j in range(len(reverseNums)):
                # match index from original
                orig_j = n - 1 - j
                if i != orig_j:
                    product *= reverseNums[j]
            res.append(product)
        return res
