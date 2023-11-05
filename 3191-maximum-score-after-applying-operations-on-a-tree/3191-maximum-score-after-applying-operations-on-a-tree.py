from typing import *
class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        
        def helper(node):
            if not graph[node]:
                return values[node]
            temp = 0
            for n in graph[node]:
                graph[n].remove(node)
                temp += helper(n)
            
            return min(temp,values[node])


        n = len(values)
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        max_score = helper(0)

        return sum(values)-max_score
