class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS recusively + hashset for visits
        #   Time  : O(n + p), where n = numCourses, p = number of prerequisites
        #   Space : O(n) for recursion stack and visited sets

        visits = set()      # {crs, ..}
        crsList = {i : [] for i in range(numCourses)} # {crs : [pre, ..], ..}
        for crs, pre in prerequisites:
            crsList[crs].append(pre)

        def dfs(crs):
            # base case#1 :
            if crs in visits:
                return False
            # base case#2 : finished the pre courses
            if len(crsList[crs]) == 0:
                return True

            visits.add(crs)

            for pre in crsList[crs]:
                if not dfs(pre):
                    return False
            
            crsList[crs] = []   # Done with pre courses. Clear the list!
            visits.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True

        

        