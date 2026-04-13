class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 'binary search' twice : left & right
        ## time :   2 * O(log n) 
        ## space:   O(1)

        def binarySearch(isLeft):
            selectedPosiition = -1 ##

            l = 0
            r = len(nums) - 1

            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    selectedPosiition = m
                    if isLeft:
                        r = m - 1
                    else:
                        l = m + 1
            
            return selectedPosiition
        

        # run binary search TWICE
        leftPosition = binarySearch(True) # left
        rightPosition = binarySearch(False) # right

        return [leftPosition, rightPosition]