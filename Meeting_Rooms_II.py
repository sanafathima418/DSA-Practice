# https://leetcode.com/problems/meeting-rooms-ii

import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        # Sort the interval array based on start time of inteval
        # Sort function replaces original list
        # Why not sort by end time - 
        # Sort by end time is taken care of by the min_heap implemented, so traverse the interal array by the start time
        intervals.sort(key = lambda x:x[0])
        
        # Create and initialize the priority queue
        p_queue = [intervals[0][1]]
        heapq.heapify(p_queue)
        
        # For every incoming interval, check if room can be reassigned or new room needs to be alloted
        for i in range(1,len(intervals)):
            # If curr time is >= top of queue, it means re-assign so pop top element from queue
            if intervals[i][0] >= p_queue[0]:
                heapq.heappop(p_queue)
            # Push new interal end time 
            heapq.heappush(p_queue,intervals[i][1])
        
        # The min rooms needed is the length of the priority queue after traversing all intervals given
        return len(p_queue)