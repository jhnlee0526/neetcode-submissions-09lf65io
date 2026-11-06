class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            num1 = nums[i]
            if i > 0 and num1 == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = num1 + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([num1, nums[l], nums[r]])
                    
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                
        return res