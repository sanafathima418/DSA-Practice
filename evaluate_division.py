# https://leetcode.com/problems/evaluate-division/

class Solution:
    def dfs(self, graph, start, end, path, visited):
        visited.append(start)
        # Get all neighbours of current node
        neighbours = graph[start] 
        answer = -1.0
        
        # Check if end is a neighbour of curr node
        if end in neighbours:
            return path * graph[start][end]

        # Traverse through all unvisited neighbours till the end
        for neigh in neighbours:
            if neigh not in visited:
                answer = self.dfs(graph, neigh, end, path*neighbours[neigh], visited)
            # IMP: to stop traversal of neighbours if at depth, end is reached
            if answer != -1.0:
                break
        return answer
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Using DFS to solve
        # Time Complexity: O(n^2)
        # Time Complexity: O(n)
        
        # Create adjacency list for the graph of equations
        graph = {}
        for i,(num,den) in enumerate(equations):
            # Create forward edge
            if num not in graph:
                graph[num] = {}
            graph[num][den] = values[i]
            
            # Create backward edge
            if den not in graph:
                graph[den] = {}
            graph[den][num] = 1 / values[i]
        
        # Traverse through queries to see evaluate division result
        res_arr = []
        for i,(num,den) in enumerate(queries):
            # 1. If both num and den not in graph - -1.0
            if num not in graph or den not in graph:
                res_arr.append(-1.0)
            # 2. If both num and den equal - 1.0
            elif num == den:
                res_arr.append(1.0)
            # 3. Perform regular division
            else:
                # Check if a path exists between num and den
                path = 1
                visited = []
                res_arr.append(self.dfs(graph,num,den, path,visited))
        
        return res_arr