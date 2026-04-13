class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ## Two Pointers
        #### time : O(n)
        #### space: O(1)
        l = 0
        r = len(numbers) - 1
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum < target:
                l += 1
            elif curr_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]  # 1-based index
        
        return []  # Edge case: No valid pair found
