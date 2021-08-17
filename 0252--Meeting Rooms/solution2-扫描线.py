class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if len(intervals) == 0:
            return True
        temp = []
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            temp.append((start, 1))
            temp.append((end, -1))

        result = 0
        temp.sort()
        count = 0
        for i in range(len(temp)):
            count += temp[i][1]
            result = max(count, result)

        if result == 1:
            return True
        else:
            return False
