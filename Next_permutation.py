# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        swap_idx = -1
        
        while right>-1 and nums[right] <= nums[right-1]:
            right -= 1
        
        if right > 0:
            left = right-1
            
            # Get 2nd largest element in decreasing seq to swap with left such that the swap_idx > left
            swap_idx = len(nums) -1
            while(swap_idx > -1 and nums[swap_idx] <= nums[left]):
                    swap_idx -= 1

            # Perform swap 
            temp = nums[left]
            nums[left] = nums[swap_idx]
            nums[swap_idx] = temp
            
        # Sort everything to the right of right idx in asc order - By reversing using 2 pointers 
        right_end = len(nums)-1
        while(right < right_end):
            temp = nums[right_end]
            nums[right_end] = nums[right]
            nums[right] = temp
            right += 1
            right_end -= 1
        
        
            