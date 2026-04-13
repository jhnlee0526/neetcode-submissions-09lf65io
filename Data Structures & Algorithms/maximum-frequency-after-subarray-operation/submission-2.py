class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # 🧮 Count how many times k already appears in nums
        cntK = nums.count(k)  # For our example: [10, 2, 3, 2, 10, 2] → cntK = 2

        res = 0  # 🔢 We'll keep track of the best frequency result here

        # 🔁 Try every value from 1 to 50 as a possible candidate to turn into k
        for i in range(1, 51):  # We'll iterate through i = 1, 2, ..., 50

            if i == k:
                continue  # 🙅 Skip k itself since it doesn’t need converting

            cnt = 0  # 🧮 How many extra k's we can create from i in a run

            # 🌀 Scan through nums to track a streak of i's we could turn into k
            for num in nums:

                # ✅ If this number is i (e.g., i = 2), it's a candidate for conversion
                if num == i:
                    cnt += 1

                # ⚠️ If this number is already k (10), converting it is meaningless → subtract
                if num == k:
                    cnt -= 1

                # 🧼 If conversion “gain” drops negative, reset (Kadane-style)
                cnt = max(cnt, 0)

                # 📈 Update best result seen so far
                res = max(res, cntK + cnt)

        return res