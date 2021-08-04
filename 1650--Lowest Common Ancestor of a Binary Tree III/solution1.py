"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        p_set = set()

        node = p
        while node:
            p_set.add(node)
            node = node.parent

        node = q
        while node:
            if node in p_set:
                return node
            node = node.parent