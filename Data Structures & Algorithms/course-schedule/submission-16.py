class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS recursively + hashset for visits
        #   Time  : O(n + p), where n = numCourses, p = number of prerequisites
        #   Space : O(n) for recursion stack and visited sets

        visits = set()  # {course, ..}
        crsList = {course : [] for course in range(numCourses)} # {course: [preCourse, ..], ..}
        for crs, pre in prerequisites:
            crsList[crs].append(pre)
        
        def dfs(crs):
            # base cases
            if crs in visits:   # cycling!
                return False
            if len(crsList[crs]) == 0:  # no more prerequisities to take
                return True
            
            visits.add(crs)
            for pre in crsList[crs]:
                if not dfs(pre):
                    return False
            
            visits.remove(crs) ## backtrack: remove from current DFS path to allow revisits from other branches
            crsList[crs] = []  # remove finished prerequisities
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
