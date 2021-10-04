class MaxStack(object):

    def __init__(self):
        self.max = []
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.max) == 0:
            self.max.append(x)
        else:
            self.max.append(max(self.max[-1], x))

    def pop(self):
        """
        :rtype: int
        """
        res = self.stack.pop()
        self.max.pop()

        return res

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.max[-1]

    def popMax(self):
        """
        :rtype: int
        """
        maxValue = self.max[-1]
        temp = []
        while self.stack[-1] != maxValue:
            temp.append(self.stack.pop())
            self.max.pop()

        self.stack.pop()
        self.max.pop()

        for i in range(len(temp) - 1, -1, -1):
            self.push(temp[i])

        return maxValue

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()