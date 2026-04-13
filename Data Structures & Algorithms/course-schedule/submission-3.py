class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # building hashmap
        preMap = { i : [] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visits for tracking to avoid cycle
        visits = set()
        
        def dfs(crs):
            # base cases
            if crs in visits:
                return False
            if preMap[crs] == []:
                return True

            visits.add(crs)
            
            for eachPre in preMap[crs]:
                if not dfs(eachPre):
                    return False
            
            visits.remove(crs)
            preMap[crs] = []
            return True            

        # invocation
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

