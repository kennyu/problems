from typing import Optional, List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}

        for (child, parent) in prerequisites:
            graph[parent].append(child)
            indegree[child] += 1

        sources = list()
        for key in indegree:
            if indegree[key] == 0:
                sources.append(key)

        visited = 0
        while len(sources) > 0:
            vertex = sources.pop()
            visited += 1
            topological_sort.append(vertex)
            for child in graph[vertex]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    sources.append(child)
        return visited == numCourses

s = Solution()
t1 = ( 2, [[1,0],[0,1]])
assert( s.canFinish(*t1) == False )
t2 = ( 2, [[1,0]] )
assert( s.canFinish(*t2) == True )
