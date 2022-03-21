# https://leetcode.com/problems/count-complete-tree-nodes/

# Using simple binary search - COME BACK and use the complete property of binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        # Class variable to track length(count) of nodes in tree
        self.length = 0
    
    def dfs(self,node):
        # Reached Null node
        if not node:
            return 
        
        # Curr node is not None, hence increment length 
        self.length += 1
        
        # If left node exists
        if node.left:
            self.dfs(node.left)
        # If right node exists
        if node.right:
            self.dfs(node.right)
    
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Complete Binary Tree: Only few right leaf nodes missing
        
        # Time Complexity - O(n)
        # Space Complexity - O(n) - For every node, a call is made
        
        self.dfs(root)
    
        return self.length
