# https://leetcode.com/problems/3sum/

class Solution:
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