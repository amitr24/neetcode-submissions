class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # If you sort this
        # You will get intervals where the start times are ascending
        # How would you know the min # of intervals though?
        intervals.sort(key = lambda x: (x[0], x[1]))
        prevEnd = intervals[0][1]
        num_intervals = 0
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                num_intervals += 1
                prevEnd = min(end, prevEnd)
        return num_intervals