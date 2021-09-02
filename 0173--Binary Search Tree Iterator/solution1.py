# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.deque = collections.deque()
        self.deque.append(root)
        self.visited = set()

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            node = self.deque.popleft()

            if node.right:
                self.deque.appendleft(node.right)
            self.visited.add(node)
            return node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.deque) != 0 and self.deque[0].left is not None and self.deque[0].left not in self.visited:
            self.deque.appendleft(self.deque[0].left)

        if len(self.deque) != 0:
            return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()