# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

# Union Find
# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution:
    
    def __init__(self):
        self.parent = []
        self.clusters = 0
    
    def find(self,node):
        # Traverse upwards till parent of the node we are trying to find is itself, 
        # We then know we have reached the root
        if self.parent[node] != node:
            return self.find(self.parent[node])
        return node
        
    def union(self,node1, node2):
        p_node1 = self.find(node1)
        p_node2 = self.find(node2)
        # If the two nodes to be combined have different parents, only then combine them
        if p_node1 != p_node2:
            self.parent[p_node2] = p_node1
            # Remove a stone
            self.clusters -= 1
    
    def removeStones(self, stones: List[List[int]]) -> int:
        # Very Imp, makes access of nodes simple as every node can be accessed using it's index
        # And no longer have to work with list indices in the array
        self.parent = [i for i in range(len(stones))]
        self.clusters = len(stones)
        
        # Check for every stone placement
        for i,curr_node in enumerate(stones):
            # Check neighbours of every stone until the current node only
            # Not sure why we check only until the current node but it works
            for j,child_node in enumerate(stones[:i]):
                # Same row or column, then detect as neighbour and combine
                if curr_node[0] == child_node[0] or curr_node[1] == child_node[1]:
                    self.union(i,j)
        
        # total stones - number of clusters formed(stones that cannot be removed)
        return len(stones) - self.clusters
        
        
            
            
        
        