class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers

        res = []
        nums.sort()
        for i in range(len(nums)):
            # skip duplicates
            if (
                i > 0 and
                nums[i] == nums[i - 1]
            ):
                continue

            # two pointers
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # keep moving on!
                    l += 1
                    while (
                        l < r and 
                        nums[l] == nums[l - 1]
                    ):
                        l += 1
                    


        return res