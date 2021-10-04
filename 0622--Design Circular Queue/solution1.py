class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = [None] * k
        self.start = None
        self.end = None
        self.k = k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        if self.end is None:
            self.start = 0
            self.end = -1
        self.end = (self.end + 1) % self.k
        self.queue[self.end] = value

        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False

        self.queue[self.start] = None
        self.start = (self.start + 1) % self.k

        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.start]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.end]

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.start is None or self.queue[self.start] is None:
            return True
        return False

    def isFull(self):
        """
        :rtype: bool
        """
        if self.end is None or self.queue[(self.end + 1) % self.k] is None:
            return False
        return True

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()