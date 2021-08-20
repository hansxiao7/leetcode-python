class StockSpanner(object):

    def __init__(self):
        self.stack = []
        self.history = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        while len(self.stack) != 0 and price >= self.history[self.stack[-1]]:
            self.stack.pop()

        if len(self.stack) != 0:
            result = len(self.history) - self.stack[-1]
        else:
            result = len(self.history) + 1

        self.history.append(price)
        self.stack.append(len(self.history) - 1)
        return result

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)