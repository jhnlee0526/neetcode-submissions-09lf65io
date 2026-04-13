class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        #   time : O(log n)
        #   space: O(1)

        l, r = 0, len(nums) - 1
        while l <= r:
            '''
            - It protects against integer overflow in languages 
                where left + right might exceed the maximum representable integer.
            - It also clearly expresses 
                “start at left and move half the distance toward right."
            '''
            m = l + (r - l) // 2
            
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1
            
