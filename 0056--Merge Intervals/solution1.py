class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort the array based on the end
        intervals.sort(key=lambda x: x[0])

        left = intervals[0][0]
        right = intervals[0][1]
        result = []

        for i in range(len(intervals) - 1):
            if intervals[i + 1][0] <= right:
                right = max(right, intervals[i + 1][1])
            else:
                result.append([left, right])
                left = intervals[i + 1][0]
                right = intervals[i + 1][1]

        result.append([left, right])

        return result
