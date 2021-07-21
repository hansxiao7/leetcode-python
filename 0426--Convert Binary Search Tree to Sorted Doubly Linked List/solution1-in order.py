"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        inorder = []
        in_order(inorder, root)

        for i in range(len(inorder)):
            left = i - 1
            right = (i + 1) % len(inorder)
            inorder[i].left = inorder[left]
            inorder[i].right = inorder[right]

        return inorder[0]


def in_order(li, node):
    if node:
        in_order(li, node.left)
        li.append(node)
        in_order(li, node.right)

