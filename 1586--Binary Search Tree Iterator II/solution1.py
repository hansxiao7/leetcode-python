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
        self.visited = set()
        self.stack = [root]
        self.arr = []
        self.pointer = -1

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack) == 0 and self.pointer == len(self.arr) - 1:
            return False
        elif self.pointer < len(self.arr) - 1:
            return True
        elif len(self.stack) != 0:
            node = self.stack[-1]

            while node.left and node.left not in self.visited:
                self.stack.append(node.left)
                node = node.left

            return True

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            if self.pointer < len(self.arr) - 1:
                self.pointer += 1
                node = self.arr[self.pointer]
            else:
                node = self.stack.pop()
                self.visited.add(node)
                self.arr.append(node)
                self.pointer += 1

                if node.right:
                    self.stack.append(node.right)

            return node.val

    def hasPrev(self):
        """
        :rtype: bool
        """
        if self.pointer > 0:
            return True
        return False

    def prev(self):
        """
        :rtype: int
        """
        self.pointer -= 1
        return self.arr[self.pointer].val

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()