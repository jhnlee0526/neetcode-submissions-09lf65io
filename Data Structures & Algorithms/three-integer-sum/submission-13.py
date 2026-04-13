class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #   Time : O(n^2)
        #       - Outer loop: O(n)
        #       - Two-pointer scan per i: O(n)
        #       - Total: O(n^2)
        #   Space: O(n)
        #       - For sorting (if not in-place) and result list

        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            
        return res

