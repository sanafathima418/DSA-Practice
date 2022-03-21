# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_dict = {}
        for i in range(len(nums)):
            if nums[i] in visited_dict:
                return [visited_dict[nums[i]],i]
            else:
                remainder = target - nums[i]
                visited_dict[remainder] = i
                
            
            