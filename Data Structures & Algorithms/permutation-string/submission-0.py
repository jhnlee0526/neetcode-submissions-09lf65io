class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## [Sliding Window] using dictionary / hashmap
        #### time : O(n)
        #### space: O(1) because 26 characters

        # Edge case: If `s1` is longer than `s2`, there is no way `s1` can be inside `s2`, so return False
        if len(s1) > len(s2):
            return False
        
        # [Step 1]: Create two lists (arrays) to count letter occurrences.
        # Since we only have lowercase letters (a-z), we make lists of size 26.
        s1Count, s2Count = [0] * 26, [0] * 26 
        
        # [Step 2]: Count the occurrences of each letter in `s1` and the first window of `s2`
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1  # Convert letter to index, update `s1` frequency
            s2Count[ord(s2[i]) - ord('a')] += 1  # Convert letter to index, update `s2` frequency
        
        # [Step 3]: Compare both arrays and count how many letter frequencies match
        matches = 0
        for i in range(26):  # We only have 26 lowercase letters
            matches += (1 if s1Count[i] == s2Count[i] else 0)  # Increase matches if counts are equal
        
        # [Step 4]: Start sliding the window across `s2`
        l = 0
        for r in range(len(s1), len(s2)):  # Move right pointer forward
            # If all 26 letters match, that means `s1` is a permutation of `s2`
            if matches == 26:
                return True
            
            # [Step 5]: Add new letter into the window (move `r`)
            index = ord(s2[r]) - ord('a')  # Convert letter to index
            s2Count[index] += 1  # Increase frequency of the new letter in `s2`
            
            # [Step 6]: If the new letter now MATCHES `s1Count`, increase matches
            if s1Count[index] == s2Count[index]:
                matches += 1
            # But if adding this letter caused MISMATCH (count went over), decrease matches
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # [Step 7]: Remove old letter from the left side of the window (`l`)
            index = ord(s2[l]) - ord('a')  # Convert letter to index
            s2Count[index] -= 1  # Decrease frequency of the letter being removed
            
            # [Step 8]: If the letter now matches again, increase matches
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If removing this letter caused mismatch (count went below), decrease matches
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            
            # [Step 9]: Move the left pointer forward (window slides)
            l += 1
        
        # [Step 10]: If we reached here, check if a valid permutation was found
        return matches == 26
