# https://leetcode.com/problems/3sum/

class Solution:
    
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    
    # Solution: 
    # 1. Sort the array in increasing order.
    # 2. Traverse through every element in the array until greater than 0(as numbers >0 cannot sum to 0 or target)
    # 3. For every element set new target as original target - current element
    # 4. Call 2 Sum II on the new target and array from i+1 to n.
    
    # Approach 2 sum II: 2 pointers - low and high
    # 1. Set low as first array element and high as last array element - Reflect states from array passed
    # 2. Until low is less than high, add low and high
    # 3. If sum is greater than target - decrement high
    # 4. If sum is lower than target - increment low
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited_dict = {}
        final_list = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                main_remainder = 0 - nums[i]
                j = i + 1
                while(j < len(nums)):
                    if nums[j] in visited_dict:
                        final_list.append([nums[i],nums[j],visited_dict[nums[j]]])
                        while(j+1 < len(nums) and nums[j+1] == nums[j]):
                            j += 1
                    else:
                        remainder = main_remainder - nums[j]
                        visited_dict[remainder] = nums[j]
                    j += 1
                visited_dict = {}
        
        return final_list
