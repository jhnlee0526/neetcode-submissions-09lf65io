class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS recursively + hashset for visits + hashmap for courses w/ prereq.
        #   time : O(n + p)
        #   space: O(n + p)
        #       -> n : number of courses, p : number of prereq
        
        visits = set()                                  # {crs, ..}
        # set up the crsMap
        crsMap = {i : [] for i in range(numCourses)}    ## {crs : [pre-req, ..], ..}
        for crs, pre in prerequisites:
            crsMap[crs].append(pre)

        def dfs(crs):
            # base case
            if crs in visits:                           # already took it. cycling detected!
                return False
            if len(crsMap[crs]) == 0:                   # done with the prerequisites for this crs
                return True

            visits.add(crs)

            # DFS the all the prerequisites for this crs
            for pre in crsMap[crs]:     
                if not dfs(pre):
                    return False

            # completed    
            visits.remove(crs)                          # done with the crs -> remove it to avoid cycling.
            crsMap[crs] = []                            # clear all the prerequisites since all completed!
            return True
            

        # inital invocation on dfs()
        for crs in range(numCourses):
            if not dfs(crs):    ##
                return False    ##
        
        return True


