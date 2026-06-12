from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        g = defaultdict(list)
        pre = prerequisites

        for v, e in pre:
            g[v].append(e)

        
        unvisit = 0
        visiting = 1
        visited = 2

        states = [unvisit] * numCourses

        def dfs(node):
            state = states[node]

            if state == visited: return True
            elif state == visiting: return False

            states[node] = visiting

            for neighbor in g[node]:
                if not dfs(neighbor):
                    return False

            states[node] = visited
            return True 


        for i in range(numCourses):
            if not dfs(i): return False
        return True




            







        

        

        










        

