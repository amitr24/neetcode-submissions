"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <=1 :
            return True
        intervals.sort(key=lambda x : (x.start, x.end))
        previous_end = 0
        for interval in intervals:
            if previous_end > interval.start or previous_end > interval.end:
                return False
            previous_end = interval.end
        return True