class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        res = 0

        cntK = nums.count(k)
        for i in range(1, 51):
            cnt = 0
            for curNum in nums:
                if curNum == i:
                    cnt += 1
                
                if curNum == k:
                    cnt -= 1

                cnt = max(cnt, 0)
                res = max(res, cnt + cntK)
        
        return res