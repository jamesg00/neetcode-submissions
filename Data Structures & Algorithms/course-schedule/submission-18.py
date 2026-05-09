class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        #build our graph first
        preMap = {i:[] for i in range(numCourses)}

        #map each course to the prerequisites
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        #visit set stores all courses along dfs path
        visit = set()

        #try to complete our course
        def dfs(crs):
            #if we already saw this course ret false, cycle
            if crs in visit: return False
            #if no pre, its safe to take
            if preMap[crs] == []: return True
            #mark course in progress
            visit.add(crs)

            #recursively check, can we complete all preprequisites?
            for pre in preMap[crs]:
                if not dfs(pre): return False
            #remove from current path ebcause we finished exploring it
            visit.remove(crs)
            #dont need to check it again once we verified it has no cycle
            preMap[crs] = []
            #no cycels found for the course
            return True
        
        #run dfs for every course 
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


            

        

        

        










        

