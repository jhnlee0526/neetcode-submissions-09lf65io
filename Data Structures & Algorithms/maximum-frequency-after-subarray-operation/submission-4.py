class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        res = 0
        cntK = nums.count(k)                # Let me start with how many k values already exist — cntK
        for i in range(1, 51):
            if i == k:
                continue
            
            cnt = 0
            for curNum in nums:
                if curNum == i:             # Add 1 if you see i (you can turn those into k using one subarray)
                    cnt += 1

                if curNum == k:             # Subtract 1 if you see k (because you can't transform those — they're already k)
                    cnt -= 1

                cnt = max(cnt, 0)           # Keep count non-negative using cnt = max(cnt, 0) → this acts like a sliding gain
                res = max(res, cnt + cntK)  # update max result 
            
        return res