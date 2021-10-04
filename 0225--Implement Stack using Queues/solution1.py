class MyStack(object):

    def __init__(self):
        self.queue = collections.deque()
        self.stack = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.queue.append(x)
        else:
            self.queue.append(self.stack.pop())
            self.queue.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) != 0:
            return self.stack.popleft()

        while len(self.queue) > 1:
            self.stack.append(self.queue.popleft())

        self.stack, self.queue = self.queue, self.stack

        return self.stack.popleft()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) != 0:
            return self.stack[0]

        while len(self.queue) > 1:
            self.stack.append(self.queue.popleft())

        self.stack, self.queue = self.queue, self.stack

        return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.queue) == 0 and len(self.stack) == 0:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()