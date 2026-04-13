class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [Topological Sort] using DFS (recursive)
        ## Time:  O(V + E), where V = numCourses & E = number of prerequisites
        ## Space: O(V + E) for graph storage + recursion stack + visited sets
        '''
        Each course can be in one of three states:
            1. visited   → course is done and already in the output
            2. visiting  → we're in the middle of exploring this course's prerequisites
            3. unvisited → we haven’t touched this course yet
        '''

        res = []

        # Build a hashmap:
        crsMap = {i: [] for i in range(numCourses)} # {crs: [pre, ], }
        for crs, pre in prerequisites:
            crsMap[crs].append(pre)

        visits = set()  # All courses we've finished exploring (safe to add to result) -> {crs, }
        cycles = set()  # Current path in DFS — used to detect if we're stuck in a cycle -> {crs, }

        def dfs(crs):
            # we found a cycle → not valid
            if crs in cycles:
                return False

            # already visited this course before, no need to do it again
            if crs in visits:
                return True

            # Mark this course as "currently exploring"
            cycles.add(crs)

            # Go through all prerequisites of this course
            for pre in crsMap[crs]:
                if not dfs(pre):  # If any prereq can't be completed, we fail
                    return False

            # Done exploring prerequisites → remove from cycle path
            cycles.remove(crs)

            # Mark this course as fully visited (safe to schedule)
            visits.add(crs)
            res.append(crs)  # Add course to output
            return True


        # Try to do DFS for every course
        for crs in range(numCourses):
            if not dfs(crs):  # If a cycle is found anywhere, return []
                return []

        return res  # Return the course order (reverse postorder works)
