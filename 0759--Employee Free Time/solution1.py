"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""


class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        temp = []
        for employee in schedule:
            for time in employee:
                start = time.start
                end = time.end

                temp.append((start, 1))
                temp.append((end, -1))

        temp.sort()
        count = 0
        result = []
        start = None
        end = None

        for i in range(len(temp)):
            count += temp[i][1]

            if count == 0:
                start = temp[i][0]

            if start is not None and count > 0:
                end = temp[i][0]
                if start != end:
                    result.append(Interval(start=start, end=end))
                start = None

        return result
