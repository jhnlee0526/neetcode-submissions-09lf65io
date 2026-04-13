class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ## [HashMap / Dictionary]
        #### time : O(n)
        #### space: O(n)
        numMap = {} # {num : index}
        for i in range(len(nums)):
            if nums[i] in numMap and abs(i - numMap[nums[i]]) <= k:
                return True
            numMap[nums[i]] = i
        
        return False

