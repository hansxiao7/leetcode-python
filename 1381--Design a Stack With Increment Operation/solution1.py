class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack = []
        self.size = maxSize
        self.incr = [0] * maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) < self.size:
            self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1

        pos = len(self.stack) - 1
        res = self.stack.pop() + self.incr[pos]

        if pos > 0:
            self.incr[pos - 1] += self.incr[pos]
        self.incr[pos] = 0

        return res

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        i = min(len(self.stack), k) - 1
        if i >= 0:
            self.incr[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)