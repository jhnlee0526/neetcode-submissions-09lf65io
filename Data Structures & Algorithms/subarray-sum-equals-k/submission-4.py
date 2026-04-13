class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [Optimized Solution] using Prefix Sums + Hashmap
        ## Time: O(n)
        ## Space: O(n) — hashmap for prefix frequencies
        cnt = 0
        prefixSum = 0
        prefixSumCnt = {}     # {prefixSum : cnt}

        prefixSumCnt[0] = 1   # base case — handles subarrays starting from index 0
        
        for num in nums:
            prefixSum += num

            if prefixSum - k in prefixSumCnt:
                cnt += prefixSumCnt[prefixSum - k]

            prefixSumCnt[prefixSum] = prefixSumCnt.get(prefixSum, 0) + 1

        return cnt


        # [Brute Force]
        ## time : O(n^2)
        ## sapce: O(1)
        cnt = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    cnt += 1
        return cnt

