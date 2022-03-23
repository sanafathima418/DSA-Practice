# https://leetcode.com/problems/strobogrammatic-number/

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        # Using 2 Pointers Technique
        # Time Complexity: O(n/2) - checking n/2 of the length of num
        # Space Complexity: O(1) - no extra space
        
        # List of possbile combinations for strobo numbers
        strobo_dict = { '0': '0', '1':'1', '8': '8', '6': '9', '9':'6' }
        
        # Initialize left and right pointers
        left = 0
        right = len(num)-1
        
        # Compare left and right in dict and string and update pointers
        while(left <= right):
            # If num not in dict or if number in strobo and number in string are different, return False
            if not num[left] in strobo_dict or not strobo_dict[num[left]] == num[right]:
                return False
            else:
                left += 1
                right -= 1
        
        # On reaching it, all chars pass the check so return True
        return True
                
                
        
        