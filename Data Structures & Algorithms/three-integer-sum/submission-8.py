class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [two pointers]
        # sort the list first
        # run for loop on the sorted list, and run two pointers inside : i, l, r
        
        res = []
        sortedNums = sorted(nums)
        
        for i in range(len(sortedNums)):
            if i > 0 and sortedNums[i] == sortedNums[i - 1]: ##
                continue
            
            l, r = i + 1, len(sortedNums) - 1
            while l < r:
                sum = sortedNums[i] + sortedNums[l] + sortedNums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([sortedNums[i], sortedNums[l], sortedNums[r]])
                    l += 1 # move just one point
                    # skip to the next until the current val is Not the same as the previous one.
                    while l < r and sortedNums[l] == sortedNums[l - 1]:
                        l += 1
        
        return res                  
