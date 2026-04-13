class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [잘모름!!] Kahn's algorithm (BFS topological sort)
        #   Time  : O(n + p), where n = numCourses, p = number of prerequisites
        #   Space : O(n) for queue, adjacency list, and in-degree tracking

        # Build adjacency list: {preCourse: [dependentCourse, ..]}
        courseMap = {course: [] for course in range(numCourses)}
        inDegree = {course: 0 for course in range(numCourses)}  # prerequisites count

        for course, pre in prerequisites:
            courseMap[pre].append(course)
            inDegree[course] += 1

        # Queue of courses with no prerequisites
        readyQueue = deque([course for course in range(numCourses) if inDegree[course] == 0])
        completed = set()  # courses we can finish

        while readyQueue:
            curCourse = readyQueue.popleft()
            completed.add(curCourse)

            for dependent in courseMap[curCourse]:
                inDegree[dependent] -= 1  # one prerequisite satisfied
                if inDegree[dependent] == 0:
                    readyQueue.append(dependent)

        # All courses must be completed
        return len(completed) == numCourses
        

        ###############################
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
