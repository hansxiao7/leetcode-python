class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        result = len(intervals)

        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if end <= prev_end:
                result -= 1
            else:
                prev_end = end

        return result
