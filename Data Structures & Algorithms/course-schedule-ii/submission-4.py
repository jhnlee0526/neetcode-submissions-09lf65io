class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [cycle detection] dfs recursively + hashmap for visits
        #   time : O(v + e), v = numCourse, e = # of pre
        #   space: O(v + e), hashsets for visits and cycle + recursion stack

        res = []

        crsMap = {crs : [] for crs in range(numCourses)}
        visits = set()
        cycles = set()

        for crs, pre in prerequisites:
            crsMap[crs].append(pre)
        
        def dfs(crs):
            # base case
            if crs in cycles:
                return False
            if crs in visits:
                return True
            
            cycles.add(crs)
            for pre in crsMap[crs]:
                if not dfs(pre):
                    return False ##
            cycles.remove(crs)

            visits.add(crs)
            res.append(crs) ##
            return True ##
        
        for crs in range(numCourses):
            if not dfs(crs):
                return [] ##
            
        return res