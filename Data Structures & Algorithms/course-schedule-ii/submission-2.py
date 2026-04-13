class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        courseMap = {course : [] for course in range(numCourses)}   # {course1: [], ..}
        for course, prereq in prerequisites:    # [[course, prereq], ...]
            courseMap[course].append(prereq)
        
        visits = set()  # {course, ...}
        cycles = set()   # {course, ...}

        def dfs(course):
            # base case
            if course in cycles:
                return False
            if course in visits:
                return True
            
            cycles.add(course)

            for prereq in courseMap[course]:
                if not dfs(prereq):
                    return False
            
            cycles.remove(course)

            visits.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return res
