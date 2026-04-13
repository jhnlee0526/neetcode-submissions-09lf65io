class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DFS recursively - Topological sort
        #   time : O(v + e), v = numCourse, e = # of pre
        #   space: O(v + e), hashsets for visits and cycle + recursion stack
        
        res = []
        # {crs : [], ...}
        crsMap = {crs : [] for crs in range(numCourses)}
        # {crs : [pre1, pre2], ...}
        for crs, pre in prerequisites:
            crsMap[crs].append(pre)
        
        visits = set()  # {crs, ...}
        cycles = set()  # {crs, ...}

        def dfs(crs):
            # edge case

            if crs in cycles: # no cycle
                return False
            if crs in visits: # it's already completed.
                return True
            
            cycles.add(crs)

            for pre in crsMap[crs]:
                if not dfs(pre):
                    return False
            
            cycles.remove(crs)
            
            visits.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res