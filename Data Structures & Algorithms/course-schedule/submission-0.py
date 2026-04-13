class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## [Graph Algorithm] - Uses **Depth First Search (DFS)** to check for cycles
        #### Time Complexity: O(n + p) → We process all courses & prerequisites once
        #### Space Complexity: O(n + p) → Storing prerequisites and visited courses
        
        # Step 1: Create a dictionary (preMap) to track prerequisites for each course
        preMap = {i: [] for i in range(numCourses)}  # Example: {0: [], 1: [], 2: []}
        for crs, pre in prerequisites:  # Loop through prerequisites
            preMap[crs].append(pre)  # Store which course depends on what
        
        # Step 2: Create a "visited" set to track courses in the current DFS path
        visitSet = set()  # Helps detect cycles in course dependencies
        
        # Step 3: Define DFS function to check if courses can be completed
        def dfs(crs):  # Recursively explore prerequisites for each course
            # If this course is already in the current DFS path, a cycle exists → Can't finish
            if crs in visitSet:
                return False  
            
            # If this course has no prerequisites, it's already "complete"
            if preMap[crs] == []:
                return True  
            
            # Step 3A: Mark this course as visited to check dependencies
            visitSet.add(crs)  
            for pre in preMap[crs]:  # Explore all prerequisites
                if not dfs(pre):  # If any prerequisite fails, return False
                    return False  
            
            # Step 3B: Remove from visited after DFS check (avoiding cycle detection issues)
            visitSet.remove(crs)  
            
            # Step 3C: Mark course as "checked" (to avoid redundant searches later)
            preMap[crs] = []  
            
            return True  # Course can be completed
        
        # Step 4: Run DFS for every course
        for each in range(numCourses):
            if not dfs(each):  # If any course has a cycle, return False
                return False  
        
        return True  # If all courses can be completed, return True