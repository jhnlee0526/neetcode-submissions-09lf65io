class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs (recursively)
        ## creating the hashmap for prerequisites
        map = { i : [] for i in range(numCourses) } # {course: [prerequisite1, prerequisite2, ...], }
        for course, prerequisite in prerequisites:
            map[course].append(prerequisite)
        
        # tracking visits to avoid cycle
        visits = set()

        def dfs(course):
            # base case
            if course in visits:
                return False # Cycle detected
            if map[course] == []:
                return True # No prereqs, done
            
            visits.add(course)
            for eachPrerequisite in map[course]:
                if not dfs(eachPrerequisite):
                    return False

            visits.remove(course)
            map[course] = [] # Mark as completed
            return True

        # calling dfs()
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True 