class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # L = 0
        # R = len(numbers) - 1

        #  L
        #  1   2   3   4.     target = 3
        #         R

        # 1 + 4 == 5 > target 
        # -> R -= 1
        # 2 + 4 == 6 == target

        # return [L, R]

        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]
