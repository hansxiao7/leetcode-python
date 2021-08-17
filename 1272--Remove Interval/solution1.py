class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        x = toBeRemoved[0]
        y = toBeRemoved[1]
        result = []

        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if end <= x or start >= y:
                result.append(interval)
            elif end > x and end <= y and start < x:
                result.append([start, x])
            elif start < y and start >= x and end > y:
                result.append([y, end])
            elif start < x and end > y:
                result.append([start, x])
                result.append([y, end])

        return result
