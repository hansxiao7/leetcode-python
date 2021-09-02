class Vector2D(object):

    def __init__(self, vec):
        """
        :type vec: List[List[int]]
        """
        self.deque = collections.deque(vec)

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return self.deque.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.deque) != 0 and isinstance(self.deque[0], list):
            li = self.deque.popleft()

            for i in range(len(li) - 1, -1, -1):
                self.deque.appendleft(li[i])

        if len(self.deque) == 0:
            return False
        return True

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()