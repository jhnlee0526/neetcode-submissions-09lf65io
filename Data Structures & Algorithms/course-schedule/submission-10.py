class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs recursively + hashmap for the crs-prereq mapping + *hashset for visits(cycle)
        #   time : O(n + p), n : number of courses, p : number of prereq
        #   space: O(n + p)
        
        # setup the hashmap crs-pre
        crsPre = {i : [] for i in range(numCourses)} # {crs: [pre, ...], }
        for crs, pre in prerequisites:
            crsPre[crs].append(pre)

        # setup the hashset visits (preventing cycle)
        visits = set()  # {crs, }

        def dfs(curCrs):    # recursively
            # base cases
            if curCrs in visits:            # detect cycling
                return False
            if crsPre[curCrs] == []:    # done taking courses!
                return True
            
            visits.add(curCrs)

            # traversing curCrs's prereqs
            for eachPre in crsPre[curCrs]:
                if not dfs(eachPre): ##
                    return False     ##
            
            visits.remove(curCrs)           # Remove from visited after DFS check (avoiding cycle detection issues)
            crsPre[curCrs] = []             # Mark as completed
            return True

        # initially invoking dfs()
        for crs in range(numCourses):
            if not dfs(crs):    ##
                return False    ##

        return True


            


        

