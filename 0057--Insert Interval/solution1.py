class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval]

        def binary_search_start(left, right, target):
            if left < right:
                mid = (left + right) // 2
                if intervals[mid][1] > target:
                    return binary_search_start(left, mid, target)
                elif intervals[mid][1] < target:
                    return binary_search_start(mid + 1, right, target)
                else:
                    return mid
            else:
                if intervals[left][1] < target:
                    left = left + 1
                return left

        def binary_search_end(left, right, target):
            if left < right:
                mid = (left + right) // 2
                if intervals[mid][0] > target:
                    return binary_search_end(left, mid, target)
                elif intervals[mid][0] < target:
                    return binary_search_end(mid + 1, right, target)
                else:
                    return mid
            else:
                if intervals[left][0] > target:
                    left = left - 1
                return left

        startPos = binary_search_start(0, len(intervals) - 1, newInterval[0])
        endPos = binary_search_end(0, len(intervals) - 1, newInterval[1])

        if startPos == len(intervals):
            return intervals + [newInterval]
        if endPos == -1:
            return [newInterval] + intervals

        result = intervals[:startPos] + [
            [min(intervals[startPos][0], newInterval[0]), max(intervals[endPos][1], newInterval[1])]] + intervals[
                                                                                                        endPos + 1:]

        return result