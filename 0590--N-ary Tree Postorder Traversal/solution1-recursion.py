"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        helper(result, root)
        return result


def helper(result, node):
    if node:
        for i in node.children:
            helper(result, i)
        result.append(node.val)