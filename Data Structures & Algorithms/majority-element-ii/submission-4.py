class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ## time : O(n)
        ## space : O(n)
        # res = []
        # dict = {}
        # for num in nums:
        #         dict[num] = dict.get(num, 0) + 1
        
        # for num, cnt in dict.items():
        #     if cnt > len(nums) / 3:
        #         res.append(num)
        
        # return res


        ## [FOLLOW UP]
        ## time : O(n)
        ## space: O(1)**
        # Start with an empty dictionary to track counts of possible candidates
        dict = {}
        # Example input
        # nums = [1, 2, 3, 1, 1, 2, 2, 2]
        for num in nums:
            # Add 1 to the count for this number (or start at 1 if it's new)
            dict[num] = dict.get(num, 0) + 1
            # For example:
            # After seeing 1 → dict = {1: 1}
            # After seeing 2 → dict = {1: 1, 2: 1}
            # After seeing 3 → dict = {1: 1, 2: 1, 3: 1}

            # If we have 2 or fewer numbers tracked, keep going
            if len(dict) <= 2:
                continue
            # If we have 3 different numbers, we need to reduce all their counts
            # Simulate "canceling them out"
            newDict = {}
            for num, cnt in dict.items():
                if cnt > 1:
                    # Keep numbers that still have some power left (count > 1)
                    # Reduce their count by 1
                    newDict[num] = cnt - 1
                    # Example: if dict = {1:1, 2:1, 3:1}, all have cnt=1 → newDict = {}
                    # If dict = {1:3, 2:2, 3:1} → newDict = {1:2, 2:1}
            # Replace old dict with the updated one (we "reset" the votes)
            dict = newDict 

        # Now we might have at most 2 candidate numbers in dict
        # But we don't yet know if they appear more than n/3 times
        res = []
        for num in dict:
            # Double-check how many times each candidate appears in the original list
            # nums.count(num) goes through the full list to count it
            if nums.count(num) > len(nums) // 3:
                # If it's a real majority (> n/3), keep it
                res.append(num)
        # Return the final result list
        return res