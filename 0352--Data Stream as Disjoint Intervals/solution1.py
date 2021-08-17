class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = {}
        self.interval = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val in self.arr:
            return

        if val - 1 not in self.arr and val + 1 not in self.arr:
            self.interval.append([val, val])
            self.arr[val] = len(self.interval) - 1
        elif val - 1 in self.arr and val + 1 not in self.arr:
            pos = self.arr[val - 1]
            self.interval[pos][1] = val
            self.arr[val] = pos
        elif val + 1 in self.arr and val - 1 not in self.arr:
            pos = self.arr[val + 1]
            self.interval[pos][0] = val
            self.arr[val] = pos
        else:
            pos = self.arr[val - 1]

            start = val - 1
            end = val + 1

            self.arr[val] = pos
            self.arr[end] = pos

            while start - 1 in self.arr:
                start = start - 1
                self.arr[start] = pos

            while end + 1 in self.arr:
                end = end + 1
                self.arr[end] = pos

            self.interval[pos] = [start, end]

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        result = set()

        for i in self.arr:
            result.add(tuple(self.interval[self.arr[i]]))
        result = list(result)
        result.sort()
        return result

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()