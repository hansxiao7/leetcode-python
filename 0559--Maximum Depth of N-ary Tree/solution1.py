"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        def helper(node):
            if node is None:
                return 0

            if node.children is None:
                return 1

            temp = 0

            for i in range(len(node.children)):
                temp = max(temp, helper(node.children[i]))

            return temp + 1

        return helper(root)