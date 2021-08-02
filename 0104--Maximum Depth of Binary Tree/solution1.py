# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return helper(root)


def helper(node):
    if node is None:
        return 0

    l = helper(node.left)
    r = helper(node.right)

    return max(l, r) + 1