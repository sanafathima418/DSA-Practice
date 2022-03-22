# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs_left(self, curr, left_len):
        print("In left")
        print(left_len)
        if not curr or (curr.left == None and curr.right == None):
            return left_len 
        if curr.left:
            return self.dfs_left(curr.left, left_len + 1)
        elif curr.right:
            return self.dfs_right(curr.right, left_len + 1)
        
    def dfs_right(self, curr, right_len):
        print("In right")
        print(right_len)
        if not curr or (curr.left == None and curr.right == None):
            return right_len
        if curr.right:
            return self.dfs_right(curr.right, right_len + 1)
        elif curr.left:
            return self.dfs_left(curr.left, right_len + 1)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left_len = 0
        right_len = 0
        
        # Diameter of a Binary Tree is distance between the left most and right most node
        if root.left:
            left_len  = self.dfs_left(root.left, left_len + 1)
        #print(left_len)
        if root.right:
            right_len = self.dfs_right(root.right, right_len + 1)
        #print(right_len)
        
        return left_len + right_len