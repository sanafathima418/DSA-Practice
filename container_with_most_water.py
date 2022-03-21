# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_area = 0
        
        while(left < right):
            curr_area = (right-left) * min(height[left], height[right])
            print(curr_area)
            if curr_area > max_area:
                max_area = curr_area
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
            
        