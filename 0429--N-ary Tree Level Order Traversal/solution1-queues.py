"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        result = []

        while len(queue) != 0:
            n = len(queue)
            temp = []
            for i in range(n):
                node = queue.pop(0)
                temp.append(node.val)
                for j in range(len(node.children)):
                    queue.append(node.children[j])

            result.append(temp)

        return result

