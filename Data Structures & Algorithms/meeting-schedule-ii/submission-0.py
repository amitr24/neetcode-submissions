"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(x.start for x in intervals)
        ends = sorted(x.end for x in intervals)
        days_needed, curr_meetings = 0, 0
        s, e = 0, 0
        while (s < len(intervals)):
            if starts[s] < ends[e]: # If at the current time, a new meeting starts
                curr_meetings += 1
                s += 1 # Move to the next start time
            else: #If a meeting ends before another starts
                curr_meetings -= 1
                e += 1
            days_needed = max(curr_meetings, days_needed)
        return days_needed