from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for v, e in prerequisites:
            graph[v].append(e)

        unvisited = 0
        visiting = 1
        visited = 2

        states = [unvisited] * numCourses

        def dfs(node):
            state = states[node]

            if state == visiting: return False
            if state == visited: return True

            states[node] = visiting

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            states[node] = visited
            return True 





        for i in range(numCourses):
            if not dfs(i): return False
        return True




            







        

        

        










        

