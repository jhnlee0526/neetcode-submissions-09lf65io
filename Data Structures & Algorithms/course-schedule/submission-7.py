class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # hashmap for crs-pre + dfs recursively

        # set up the map
        crsPreMap = {crs : [] for crs in range(numCourses)} # {crs : [pre, ...], }
        for crs, pre in prerequisites:
            crsPreMap[crs].append(pre)

        visits = set() # avoid cycle : [crs, ...]

        def dfs(crs):
            # base case
            if crs in visits: # in cycle
                return False
            if not crsPreMap[crs]: # len(cresPreMap[crs]) == 0
                return True
            
            visits.add(crs)
            
            # check each pre in the current crs
            for curPre in crsPreMap[crs]:
                if not dfs(curPre):
                    return False
            
            visits.remove(crs)
            crsPreMap[crs] = []
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

