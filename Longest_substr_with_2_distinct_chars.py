# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/submissions/

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 3:
            return n
        
        count_dict = {}
        left, right = 0, 0
        max_len = 0
        
        while(right<n):
            # Dictionary contains char with rightmost idex
            count_dict[s[right]] = right
            # Move right pointer
            right += 1
            
            # Atmost 3 elements in dict at a time
            if len(count_dict) == 3:
                # Delete farthest element(backwards) traversed so far
                del_idx = min(count_dict.values())
                del count_dict[s[del_idx]]
                
                # Move left pointer 
                left = del_idx + 1
            
            # Update max len after every iteration
            max_len = max(max_len, right-left)
                
        return max_len