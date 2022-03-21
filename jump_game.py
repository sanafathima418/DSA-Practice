# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # Greedy Approach - O(n)
        if not nums:
            return False

        i = 0
        max_index = nums[i]
        # Calculate max index you can reach for every iteration and compare against local maxima, 
        # update local maxima if curr max is grater
        while i < len(nums) and i <= max_index:
            new_index = nums[i]+i
            max_index = max(max_index, new_index)
            i += 1
        # If end reached, then destination is possible
        if i == len(nums):
            return True
        else:
            return False