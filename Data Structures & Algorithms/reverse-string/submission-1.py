class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ## reverse method
        #### time : O(n)
        #### space: O(1) 
        # s.reverse() 

        ## two pointers
        #### time : O(n)
        #### space: O(1)
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1