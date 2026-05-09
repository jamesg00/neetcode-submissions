class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereq = {i:[] for i in range(numCourses)}
        

        #just basically map each course into map
        for pre, crs in prerequisites:
            prereq[crs].append(pre)

        visit = set()

        #magic happens
        def dfs(crs):
            #if we saw ts
            if crs in visit: return False
            #is valid!
            if prereq[crs] == []: return True

            #aight i saw it
            visit.add(crs)

            #can we complete all prerequisites
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
                
            #if we can remove from visit
            visit.remove(crs)
            #set it to empty so no cycle
            prereq[crs] = []
            #no cycles at all
            return True
        
        #run dfs for evry crs
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True 
        

