class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ## [HashMap / Dictionary]
        #### time : O(n)
        #### space: O(n)
        # numMap = {} # {num : index}
        # for i in range(len(nums)):
        #     if nums[i] in numMap and abs(i - numMap[nums[i]]) <= k:
        #         return True
        #     numMap[nums[i]] = i
        
        # return False


        ## [Sliding Window] using HashSet : set()
        #### time : O(n) → Iterate nums once
        #### space: O(k) → Store at most `k` elements in the set
        window = set()
        l = 0
        for r in range(len(nums)):
            if len(window) > k: # Ensure window size ≤ k
                window.remove(nums[l]) # Remove old entry
                l += 1 # Move left pointer
            
            if nums[r] in window:
                return True
            else:
                window.add(nums[r])

        return False

