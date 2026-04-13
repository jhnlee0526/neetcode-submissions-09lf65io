class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i : [] for i in range(numCourses) } # {crs : [pre, ...], }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visitSet.remove(crs)
            preMap[crs] = []
            
            return True

        for cnt in range(numCourses):
            if not dfs(cnt):
                return False
        return True