import heapq


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []  # last half
        self.maxHeap = []  # first half
        self.count = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.count += 1
        if len(self.minHeap) == 0:
            heapq.heappush(self.minHeap, num)
        elif len(self.minHeap) > len(self.maxHeap):
            if num > self.minHeap[0]:
                temp = heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, num)
                heapq.heappush(self.maxHeap, -temp)
            else:
                heapq.heappush(self.maxHeap, -num)
        else:
            if num > -self.maxHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                temp = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -temp)
                heapq.heappush(self.maxHeap, -num)

    def findMedian(self):
        """
        :rtype: float
        """
        if self.count % 2 == 0:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            return self.minHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()