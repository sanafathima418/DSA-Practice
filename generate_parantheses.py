# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        string_stack = []
        pair_list = []
        
        # Time Complexity: Order of O(4^N)
        # Space Complexity: Order of O(4^N)
        
        # Solved using Backtracking
        # 1. Base Case
        # 2. Adding open bracket
        # 3. Adding Closing Bracket
        
        def backtrack(openB,closeB):
            if openB == n and closeB == n:
                # Base Case - If open and close counts are n, return
                pair_list.append("".join(string_stack))
                return
            
            # Could have a scenario where for one string both a open or close bracket could be added in next step
            # Hence use if and if for both cases
            if openB < n:
                # Add open bracket only if open count is less than n
                string_stack.append('(')
                backtrack(openB+1, closeB)
                string_stack.pop()
                
            if closeB < openB:
                # Add close bracket only when open count is more than close count
                string_stack.append(')')
                backtrack(openB, closeB+1)
                string_stack.pop()
        
        # Initial call to backtrack
        backtrack(0,0)
        return pair_list