# https://leetcode.com/problems/backspace-string-compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        # Revisit to solve this completely - with O(1) space complexity
        
        del_s = 0
        del_t = 0
        
        s = s[::-1]
        t = t[::-1]
        
        # Get greatest length
        n = len(s) if len(s) > len(t) else len(t)
        
        # i iterates over the longest string
        i = 0
        j = 0
        while(i<n):
            if s[i] == '#' or t[j] == '#':
                if s[i] == '#':
                    del_s += 1
                    i += 1
                if t[j] == '#':
                    del_t += 1
                    j += 1
            else:
                i += del_s
                j += del_t
                del_s = 0
                del_t = 0  
                if s[i] != t[j]:
                    return False
                i += 1
                j += 1
                
        return True
                
            
            
                
                
            