class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS recursively with cycle detection
        #   time : O(N + P) where N = numCourses, P = len(prerequisites)
        #   space: O(N + P) for courseMap and recursion stack

        # edge case
        if not prerequisites:
            return True

        visits = set()      # {crs, ..} -> cycling detection

        courseMap = {}      # {course : [prerequisite, ..], ..}
        for crs, pre in prerequisites:
            if crs not in courseMap:
                courseMap[crs] = []
            courseMap[crs].append(pre)

        def dfs(crs):
            # base case
            if crs in visits:               # cycling detected!
                return False
            if (
                crs not in courseMap or     # the course doesn't have prerequisites
                not courseMap[crs]          # finished all prerequisites
            ):  
                return True
            
            visits.add(crs)

            # traverse dfs() with prerequisite
            for pre in courseMap[crs]:
                if not dfs(pre):
                    return False
            
            # clear the finished course and its prerequisites
            visits.remove(crs)
            courseMap[crs] = []

            # done with the course
            return True

        # initial start on dfs() with course
        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True
        