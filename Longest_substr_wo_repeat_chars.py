# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        
        max_len = 0
        if s:
            if len(s) == 1:
                return 1
            sub_str = s[left]
            

            # Check for len of longest substr using 2 pointers
            while(right+1<len(s)):
                curr_char = s[right+1]
                if curr_char in sub_str:
                    # If repeat : Move left pointers until no duplicates 
                    if s[left] == curr_char:
                        left += 1
                    else:
                        c = 0
                        while(sub_str[c] != curr_char):
                            left += 1
                            c += 1
                        left += 1
                    right += 1
                    if left != right:
                        sub_str = s[left:right+1]
                    else:
                        sub_str = curr_char

                else:
                    # If no repeat: Move right index and update max len as we go
                    right += 1
                    sub_str += curr_char
                if len(sub_str) > max_len:
                    max_len = len(sub_str)
                print(sub_str)
        return max_len