import heapq


class FreqStack(object):

    def __init__(self):
        self.counts = {}
        self.pos = 0
        self.heap = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.counts[val] = self.counts.get(val, 0) + 1
        heapq.heappush(self.heap, (-self.counts[val], -self.pos, val))
        self.pos += 1

    def pop(self):
        """
        :rtype: int
        """
        _, _, val = heapq.heappop(self.heap)
        self.counts[val] -= 1

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()