class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.left = 0
        self.right = 0
        self.flag = True

    def next(self):
        """
        :rtype: int
        """
        if self.flag and self.left < len(self.v1):
            result = self.v1[self.left]
            self.left += 1
        elif not self.flag and self.right < len(self.v2):
            result = self.v2[self.right]
            self.right += 1

        elif self.left == len(self.v1) and self.right < len(self.v2):
            result = self.v2[self.right]
            self.right += 1
        elif self.left < len(self.v1) and self.right == len(self.v2):
            result = self.v1[self.left]
            self.left += 1
        elif self.left == len(self.v1) and self.right == len(self.v2):
            return None

        self.flag = not self.flag
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.left < len(self.v1) or self.right < len(self.v2):
            return True
        else:
            return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())