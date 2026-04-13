class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ## four pointers (two pointers)
        #### time : O(n^2) = O(n logn) + O(n^2)
        #### space: O(m) for the output ~ O(1)
        res = []
        nums.sort()
        for i in range(len(nums)):
            # skip to the next if the current val is the same as the previous
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, len(nums)):
                # skip to the next if the current val is the same as the previous
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum > target:
                        r -= 1
                    elif sum < target:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        # skip to the next if the current val is the same as the previous
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
            
        return res
                        

            