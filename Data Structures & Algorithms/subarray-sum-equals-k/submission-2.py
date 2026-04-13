class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ## [Brute Force]
        #### time : O(n^2)
        #### space: O(1)
        # cnt = 0
        # for i in range(len(nums)):
        #     total = 0
        #     for j in range(i, len(nums)):
        #         total += nums[j]
        #         if total == k:
        #             cnt += 1

        # return cnt


        ## [OPTIMAL SOLUTION - hash map]
        #### time : O(n)
        #### space: O(n)
        res = 0                 # Number of subarrays summing to k found so far
        curSum = 0              # Running prefix sum of nums elements
        prefixSums = {0: 1}     # Dictionary to count how many times a prefix sum occurs
                                # Initially, prefix sum 0 occurs once (empty subarray)

        for num in nums:
            curSum += num       # Add current number to running sum
            # After first iteration: curSum = 1
            # After second iteration: curSum = 3
            # After third iteration: curSum = 6

            diff = curSum - k   # The sum we want to find in prefixSums to form subarray with sum k
            # After first iteration: diff = 1 - 3 = -2
            # After second iteration: diff = 3 - 3 = 0
            # After third iteration: diff = 6 - 3 = 3

            # Check if there is a prefix sum that equals diff
            # If yes, add its count to result (means subarray(s) found that sum to k)
            res += prefixSums.get(diff, 0)
            # Iteration 1: prefixSums.get(-2,0) = 0 → res = 0
            # Iteration 2: prefixSums.get(0,1) = 1 → res = 0 + 1 = 1
            # Iteration 3: prefixSums.get(3,1) = 1 → res = 1 + 1 = 2

            # Record/update the count of the current prefix sum in the dictionary
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
            # Iteration 1: prefixSums[1] = 1 + 0 = 1 → prefixSums = {0:1, 1:1}
            # Iteration 2: prefixSums[3] = 1 + 0 = 1 → prefixSums = {0:1, 1:1, 3:1}
            # Iteration 3: prefixSums[6] = 1 + 0 = 1 → prefixSums = {0:1, 1:1, 3:1, 6:1}

        return res
