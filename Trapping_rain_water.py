# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        water_vol = 0
        left, right = 0, len(height) - 1
        left_max,right_max = 0, 0
        
        while(left < right):
            if height[left] < height[right]:
                # Update leftmax
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    water_vol += left_max - height[left]
                left += 1
            else:
                # Update rightmax
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water_vol += right_max - height[right]
                right -= 1
        return water_vol