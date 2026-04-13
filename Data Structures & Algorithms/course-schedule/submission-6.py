class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs (recursively)
        
        # set up the hashmap for the courses and prerequisites
        crsMap = {i : [] for i in range(numCourses)} # {crs : [pre, ], }
        for crs, pre in prerequisites:
            crsMap[crs].append(pre)

        # for preventing from going in cycle
        visits = set() # {crs, }

        def dfs(crs):
            if crs in visits:
                return False
            if len(crsMap[crs]) == 0:
                return True
            
            visits.add(crs)
            for pre in crsMap[crs]:
                if not dfs(pre):
                    return False
            
            visits.remove(crs)
            crsMap[crs] = []
            return True

        # calling dfs() initially
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

