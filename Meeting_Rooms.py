# https://leetcode.com/problems/meeting-rooms

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        min_rooms = 1
        
        # Time Complexity O(nlogn)
        # Space Complexity O(1)
        
        # 1. Sort the array based on end time
        new_intervals = sorted(intervals,key=lambda x: x[1])
        
        # For every interval:
        for i in range(1,len(new_intervals)):
            # Check if curr interval start time is less than prev interval end time
            if new_intervals[i][0] < new_intervals[i-1][1]:
                # Return False
                return False
        
        # If it reached the end, return True as the person can attend all meetings        
        return True
                
        
