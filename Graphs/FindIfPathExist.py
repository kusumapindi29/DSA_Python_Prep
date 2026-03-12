"""
Problem: Find if Path Exists in Graph
Platform: LeetCode
Pattern: Graph DFS

Time Complexity: O(V + E)
- V = number of vertices
- E = number of edges
- In the worst case, DFS visits every vertex and explores all edges.

Space Complexity: O(V)
- Due to the visited set and recursion stack.
"""
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for i in range(0,n):
            graph[i]=[]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
        visited=set()
        visited.add(source)
        def dfs(node):
            if node==destination:
                return True
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True 
            return False
        return dfs(source)
        
