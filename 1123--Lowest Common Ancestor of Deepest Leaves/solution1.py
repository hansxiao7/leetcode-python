# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        node = root
        while node:
            l = height(node.left)
            r = height(node.right)

            if l == r:
                return node
            elif l > r:
                node = node.left
            else:
                node = node.right


def height(node):
    if node is None:
        return 0

    l = height(node.left)
    r = height(node.right)

    return max(l, r) + 1