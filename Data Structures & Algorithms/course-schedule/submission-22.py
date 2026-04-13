class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Graph: Cycling detection - DFS recursively + hashmap for visits
        #   Time : O(v + e); v = numCourses, e = # of prerequisites
        #   Space: O(v + e); recursion stacks + hashsets for visits and cycles

        # {crs, ...}
        visits, cycles = set(), set()
        # {crs : [pre, ..], ..}
        crsMap = {crs : [] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            crsMap[crs].append(pre)
        
        def dfs(crs):
            # base cases
            if crs in visits:   # completed -> YES
                return True
            if crs in cycles:   # cycling -> NO
                return False
            
            cycles.add(crs)
            for pre in crsMap[crs]:
                if not dfs(pre):
                    return False
            cycles.remove(crs)

            visits.add(crs) # completed
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True
        
        
