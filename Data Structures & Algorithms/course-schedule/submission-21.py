class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [Cycle detection] dfs recursively + hashmap for visits
        #   time : O(v + e), v = numCourse, e = # of pre
        #   space: O(v + e), hashsets for visits and cycle + recursion stack

        # {crs : pre-list, crs : [pre1, pre2, ..], ..}
        crsMap = {crs : [] for crs in range(numCourses)} 
        visits = set()  # {crs, ..}
        cycles = set()   # {crs, ..}

        for crs, pre in prerequisites:
            crsMap[crs].append(pre)

        def dfs(crs):
            # base case
            if crs in visits:   # completed -> yes
                return True
            if crs in cycles:    # cycling -> no
                return False

            cycles.add(crs)
            for pre in crsMap[crs]:
                if not dfs(pre):
                    return False
                    
            cycles.remove(crs)

            visits.add(crs)
            return True
            

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
        
        

        