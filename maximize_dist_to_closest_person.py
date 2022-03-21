# https://leetcode.com/problems/maximize-distance-to-closest-person/

class Solution:
    
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = 0
        i = 0
        j = 1
        
        while(j<len(seats)):
            if i==0 and seats[i] == 0:
                # Starts with 0 and ends with 1
                max_dist = max(max_dist,j)
            if j == len(seats)-1 and seats[j] == 0:
                # End with 0
                max_dist = max(max_dist,(j - i))
            if j == len(seats)-1 and seats[j] == 1:
                # End with 1
                max_dist = max(max_dist,int((j-i)/2))
            elif seats[j] == 1:
                # Between 1
                max_dist = max(max_dist,int((j-i)/2))
                i = j
            j += 1
        return max_dist
                
            