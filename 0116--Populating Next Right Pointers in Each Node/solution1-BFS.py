"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # use bfs with O(N) space
        if root is None:
            return None

        queue = [root]

        while len(queue) != 0:
            n_q = len(queue)
            prev = None

            for i in range(n_q):
                node = queue.pop(0)

                if prev:
                    prev.next = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                prev = node

        return root