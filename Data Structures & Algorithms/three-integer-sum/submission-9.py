class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers
        #   time : O(n^2)
        #   space: O(n)

        res = []
        # sort the list
        sortedNums = sorted(nums)           # time : O(n logn)

        for pt in range(len(sortedNums)):   # time : O(n^2)
            # skip any duplicates
            if pt > 0 and sortedNums[pt] == sortedNums[pt - 1]: ##
                continue

            # two pointers
            l, r = pt + 1, len(sortedNums) - 1
            while l < r:
                sum = sortedNums[pt] + sortedNums[l] + sortedNums[r]

                if sum < 0:
                    l += 1
                    
                elif sum > 0:
                    r -= 1

                else:   ##
                    res.append([sortedNums[pt], sortedNums[l], sortedNums[r]])
                    l += 1  # keep moving just one point
                    while l < r and sortedNums[l] == sortedNums[l - 1]: # skip to the next until the current val is Not the same as the previous one.
                        l += 1

        return res