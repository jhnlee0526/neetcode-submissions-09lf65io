class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # hashmap (crs-pres) + hashset for visits(cycle) + dfs recursively
        
        # set up hashmap
        crsMap = {i : [] for i in range(numCourses)} # {crs : [pre, ...], }
        for crs, pre in prerequisites:
            crsMap[crs].append(pre)
        
        # set up hashset for preventing cycle
        visits = set() # [crs, ]

        # dfs recursively
        def dfs(curCrs):
            # base case
            if curCrs in visits:    # cycling
                return False
            if not len(crsMap[curCrs]): # done!
                return True
            
            visits.add(curCrs)
            
            for pre in crsMap[curCrs]:
                if not dfs(pre):
                    return False
            
            visits.remove(curCrs)
            return True
            

        # init dfs
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
