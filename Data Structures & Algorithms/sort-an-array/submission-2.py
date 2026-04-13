class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ## Brute Force : time O(n^2) space O(1)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             j += 1
        #     i += 1
        # return nums

        ## Insertion Sort: time O(n^2), space O(1)
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0 and nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j -= 1
        return nums

        