class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        '''❓ Is this sliding window?
        🤔 Not quite — more of a Kadane-style greedy scan for streaks'''
        ## ⏱️ Time Complexity: O(50 · n)
        '''We loop through 50 values (1 to 50), and inside that loop, we scan the entire list
        So total time = 50 * n = O(n), since 50 is constant'''
        ## 📦 Space Complexity: O(1)
        '''We only use a few counters — no extra memory based on input size'''
        
        res = 0  # 🔢 We'll keep track of the best frequency result here
        
        # 🧮 Count how many times k already appears in nums
        cntK = nums.count(k)

        # 🔁 Try every value from 1 to 50 as a possible candidate to turn into k
        for i in range(1, 51):
            if i == k:
                continue  # 🙅 Skip if the value is already k — we don’t need to transform it

            cnt = 0  # 🧮 Temporary counter to track how many extra k's we can create

            # 🌀 Go through the list and look for runs of i's to transform into k
            for num in nums:
                if num == i:
                    cnt += 1  # ✅ Found a number we can convert to k → boost count

                if num == k:
                    cnt -= 1  # ⚠️ Already k — don’t transform it → reduce the gain

                cnt = max(cnt, 0)  # 🧼 Reset if the gain becomes negative (Kadane-style)

                res = max(res, cntK + cnt)  # 📈 Update result if this run gives a better k frequency

        return res  # 🎯 Final answer: maximum number of k's possible after one subarray operation