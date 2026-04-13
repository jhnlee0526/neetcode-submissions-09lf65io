class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # {crs1 : [pre1, pre2], ..}
        crsMap = {crs : [] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            crsMap[crs].append(pre)

        cycles = set()  # {crs, ..}
        visits = set()  # {crs, ..}

        def dfs(crs):
            # base case
            if crs in visits:   # already completed
                return True
            if crs in cycles:   # no cycle
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