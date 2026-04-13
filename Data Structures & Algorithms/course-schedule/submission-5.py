class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs (recursively)

        ## set up hashmap for course and prerequisites
        crsMap = {i : [] for i in range(numCourses)} # {crs: [pre, ], }
        for crs, pre in prerequisites:
            crsMap[crs].append(pre)
        
        ## set up visits to avoid any cycle
        visits = set()

        def dfs(crs): # recursive
            ## base cases
            if crs in visits:
                return False
            if crsMap[crs] == []:
                return True
            
            visits.add(crs)
            ## check each of the current prerequisites
            for curPre in crsMap[crs]:
                if not dfs(curPre):
                    return False
            
            ## when everything is alright, remove the crs from visits, and clear the map
            visits.remove(crs)
            crsMap[crs] = []
            return True

        # calling dfs()
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
            

            