# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def __init__(self):
        self.adj_list = {}
        self.visited_dict = {}
        self.topo_st = []
    
    # Using DFS and Topo Sort
    # TO DO: Explore solving this using Kahn's Algorithm(with node)
    # Time Complexity: O(V+E)
    # Space Complexity: O(V+E)
    
    def dfs(self,curr_node,isPossible):
        
        if not isPossible:
            # If cycle flag set, backtrack
            return False 
        
        elif not self.visited_dict[curr_node]:
            # If node not visited, set flag for partial visited
            self.visited_dict[curr_node] = 1
            
            # Traverse through neighbours of current node 
            if self.adj_list[curr_node]:
                for node in self.adj_list[curr_node]:
                    # IMPORTANT: If child node is partially visited, only then detect cycle
                    if self.visited_dict[node] == 1:
                        return False
                    else:
                        isPossible = self.dfs(node, isPossible)
            
            # Mark node as fully visited
            self.visited_dict[curr_node] = 2
            # Append prerequisite order to topo sort stack
            self.topo_st.append(curr_node)
        
        return isPossible
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Cycle Flag
        isPossible = True
        
        # If no courses
        if not prerequisites:
            return [k for k in range(0,numCourses)][::-1]
        
        # Create Adjacency List 
        #[main_course,sub_course]
        for i in range(len(prerequisites)):
            # Check if main course in adj list
            if prerequisites[i][0] in self.adj_list:
                self.adj_list[prerequisites[i][0]].append(prerequisites[i][1])
            else:
                 self.adj_list[prerequisites[i][0]] = [prerequisites[i][1]]
            # Check if sub course in adj list
            if not prerequisites[i][1] in self.adj_list:
                 self.adj_list[prerequisites[i][1]] = []
        
        # If number of courses in prereqs are lesser, add the missing courses
        if len(self.adj_list) < numCourses:
            for i in range(numCourses):
                if i not in self.adj_list:
                    self.adj_list[i] = []
                    
        # Create visited array with all courses initialized to 0
        self.visited_dict = {k: 0 for k in self.adj_list.keys()}
        
        # Traverse over Adj list using DFS and Topo sort
        for key,value in self.adj_list.items():
            if not self.visited_dict[key]:
                isPossible = self.dfs(key,isPossible)
                
        # Return empty array if cycle exists
        if not isPossible:
            return []
                             
        return self.topo_st
        
        
            
        
        