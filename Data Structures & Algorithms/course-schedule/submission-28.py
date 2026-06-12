from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        pre = prerequisites

        for v, e in pre:
            graph[v].append(e)


        unvisited = 0
        visiting = 1
        visited = 2

        states = [unvisited] * numCourses #number of courses bro!

        def dfs(node):

            state = states[node]

            if state == visiting: return False
            if state == visited: return True

            states[node] = visiting

            for neighbor in graph[node]:
            #if not dfs bro!
                if not dfs(neighbor): return False

            states[node] = visited
            return True 
            

        
        for i in range(numCourses):
            if not dfs(i): return False

        return True






            







        

        

        










        

