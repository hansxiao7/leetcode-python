class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval]

        intervals.append(newInterval)
        intervals.sort()

        result = []

        i = 0

        while i < len(intervals) - 1:
            start = intervals[i][0]
            end = intervals[i][1]

            while i < len(intervals) - 1 and intervals[i + 1][0] <= end:
                end = max(end, intervals[i + 1][1])
                i += 1

            i += 1
            result.append([start, end])

        if result[-1][1] < intervals[-1][1]:
            result.append(intervals[-1])

        return result