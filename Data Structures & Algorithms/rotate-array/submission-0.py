class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## two pointers : Using Reverse!
        #### time : O(n)
        #### space: O(1)
        ## 1. reverse the whole array
        ## 2. divide the array into two, and reverse each : l ~ k - 1, k ~ r
        
        # (no rotation) – Your logic correctly skips unnecessary reversals
        k %= len(nums)
        # reversing the whole array: [8, 7, 6, 5, 4, 3, 2, 1]
        self.reverse(nums, 0, len(nums) - 1)
        # devide the array into two and reversing each: k= 4, [8, 7, 6, 5 // 4, 3, 2, 1]
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

        
    def reverse(self, arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1