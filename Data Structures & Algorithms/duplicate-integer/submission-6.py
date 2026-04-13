class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a dictionary for mapping: dict = {item: cnt}
        # go thru iteration on nums
            # if current item doesn't exist in dic, add current item to nums with 1 count.
            # else, return True
        # return False

        ## Using regular dictionary : time O(n), space O(n)
        # dict = {}
        # for n in nums:
        #     if n not in dict:
        #         dict[n] = 1
        #     else:
        #         return True
        # return False

        ## Using defaultdict : time O(n), space O(n)
        # dict = defaultdict(int)
        # for n in nums:
        #     if n not in dict:
        #         dict[n] = 1
        #     else:
        #         return True
        # return False

        ## Using set: time O(n), space O(n)
        dict = set()
        for n in nums:
            if n not in dict:
                dict.add(n)
            else:
                return True
        return False

