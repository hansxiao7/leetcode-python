class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 1:
            return 1

        temp = []
        for interval in intervals:
            start = interval[0]
            end = interval[1]

            temp.append((start, 1))
            temp.append((end, -1))

        temp.sort()
        count = 0
        result = 0

        for i in range(len(temp)):
            count += temp[i][1]
            result = max(result, count)

        return result
