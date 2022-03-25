# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # Using backtracking
        # Time Complexity : O((4^n)*n):
        # 4^n - Cause max chars of all digits is 4. for every n we check 4 digits
        # *n - Cause we check every digit 
        # Space Complexity: O(N)
        
        phone_dict = {
                     '2':['a','b','c'],
                     '3':['d','e','f'],
                     '4':['g','h','i'],
                     '5':['j','k','l'],
                     '6':['m','n','o'],
                     '7':['p','q','r','s'],
                     '8':['t','u','v'],
                     '9':['w','x','y','z'],
                     }
        
        combo_list = []
        
        # Backtrack function
        def backtrack(path,curr_idx):
            # Base Case to check for leaf node
            if len(path) == len(digits):
                # If leaf node, add to comb list 
                combo_list.append("".join(path))
                return 
            
            # Get all characters corresponding to current number
            curr_digit = phone_dict[digits[curr_idx]]
            # For every level, check all characters
            for char_digit in curr_digit:
                # Append current level character to path
                path.append(char_digit)
                # Check for characters on next level(next digit)
                backtrack(path, curr_idx+1)
                # After returning from recursion, pop the next level character 
                # This is to retain only the character of current level
                path.pop()
        
        # Return Empty if no digits in input
        if not digits:
            return []
        
        # Return the characters of the digit itself if only 1 digit
        if len(digits) == 1:
            return phone_dict[digits[0]]
        
        # Traverse through digits string, one number at a time
        backtrack([],0)
        
        return combo_list