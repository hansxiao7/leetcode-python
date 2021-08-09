class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])

        temp = 1
        end = intervals[0][1]
        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0] < end:
                continue
            else:
                temp += 1
                end = intervals[i][1]

        return n - temp