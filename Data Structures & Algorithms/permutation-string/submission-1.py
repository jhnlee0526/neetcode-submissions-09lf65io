class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## [Sliding Window] using dictionary / hashmap
        #### time : O(n)
        #### space: O(1) because 26 characters
        # If `s1` is longer than `s2`, there's no way `s1` can be inside `s2`
        if len(s1) > len(s2): 
            return False

        # Step 1: Create two lists (arrays) to count letter frequencies.
        # Since we only care about lowercase letters ('a' to 'z'), we make lists of size 26.
        s1Count = [0] * 26
        s2Count = [0] * 26

        # Step 2: Count occurrences of each letter in `s1` and first window of `s2`
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1  # Convert letter to index, update `s1` frequency
            s2Count[ord(s2[i]) - ord('a')] += 1  # Convert letter to index, update `s2` frequency

        # Step 3: Compare both arrays and count how many letter frequencies match
        matches = 0
        for i in range(26):  # We only have 26 lowercase letters
            if s1Count[i] == s2Count[i]:  # If count of a letter matches in both arrays
                matches += 1  # Increase matches

        # Step 4: Start moving the sliding window across `s2`
        l = 0
        for r in range(len(s1), len(s2)):  # `r` moves forward, expanding the window
            # If all 26 letters match, that means `s1` is a permutation of `s2`
            if matches == 26:
                return True

            # Step 5: Add new letter at `r`
            rightIndexS2 = ord(s2[r]) - ord('a')  # Convert letter to index
            s2Count[rightIndexS2] += 1  # Increase frequency of the new letter in `s2`

            # Step 6: If the new letter now matches `s1Count`, increase matches
            if s1Count[rightIndexS2] == s2Count[rightIndexS2]:
                matches += 1
            # If adding this letter made its count **go over the expected value**, decrease matches
            elif s1Count[rightIndexS2] + 1 == s2Count[rightIndexS2]:
                matches -= 1

            # Step 7: Remove old letter from the left side of the window (`l`)
            leftIndexS2 = ord(s2[l]) - ord('a')  # Convert letter to index
            s2Count[leftIndexS2] -= 1  # Decrease frequency of the letter being removed
            
            # Step 8: If the letter count now **matches** again, increase matches
            if s1Count[leftIndexS2] == s2Count[leftIndexS2]:
                matches += 1
            # If removing this letter made its count **go below the expected value**, decrease matches
            elif s1Count[leftIndexS2] - 1 == s2Count[leftIndexS2]:
                matches -= 1
            
            # Step 9: Move the left pointer forward (shrink the window)
            l += 1

        # Step 10: If we reached here, check if a valid permutation was found
        return matches == 26
