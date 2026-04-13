class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        """
        🔸 Time: O(n log n + u * v³)
        (Usually dominated by sorting and 3-sequence generation)
            O(n log n)   ← sort visits
            + O(n)       ← build user map
            + O(u * v³)  ← generate 3-sequences per user
            + O(p)       ← scan counts to find max

        🔸 Space: O(n + p)
            O(n)         ← visit list and user map
            + O(p)       ← pattern counts
        """
        
        # Step 1: Combine input data and sort by timestamp
        # Each entry is (timestamp, username, website)
        arr = list(zip(timestamp, username, website))
        arr.sort()  # Sort so that we get correct chronological order

        # Step 2: Build user → list of websites visited in order
        userSiteMap = {}  # Dictionary to store user's visit history

        for _, user, site in arr:
            if user not in userSiteMap:
                userSiteMap[user] = []  # Initialize list if user not seen
            userSiteMap[user].append(site)  # Append current site to the user's history

        # Step 3: Count how many users have each 3-sequence pattern
        counts = {}  # Dictionary to store pattern → number of users who had it

        for curUser in userSiteMap:
            patterns = set()  # Use a set to avoid counting duplicates for the same user
            curSites = userSiteMap[curUser]  # List of websites visited by current user

            # Generate all 3-sequences (i < j < k) from current user's sites
            for i in range(len(curSites)):
                for j in range(i + 1, len(curSites)):
                    for k in range(j + 1, len(curSites)):  # ✅ fixed k from k+1 to j+1
                        patterns.add((curSites[i], curSites[j], curSites[k]))  # Store as tuple

            # Count each unique 3-sequence for this user (only once per user)
            for curPat in patterns:
                if curPat not in counts:
                    counts[curPat] = 0
                counts[curPat] += 1

        # Step 4: Find the pattern with the highest count
        # In case of a tie, choose lexicographically smallest pattern
        maxCount = 0
        res = []  # Final result pattern as a list

        for curPat in counts:
            curCount = counts[curPat]
            curPatternList = [curPat[0], curPat[1], curPat[2]]  # Convert tuple to list for comparison

            # Update result if this pattern has higher count
            # Or same count but lexicographically smaller
            if (
                curCount > maxCount or
                (curCount == maxCount and curPatternList < res)
            ):
                maxCount = curCount
                res = curPatternList

        # Step 5: Return the result pattern (most common 3-sequence as a list)
        return res

