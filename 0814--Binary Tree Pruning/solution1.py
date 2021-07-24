# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return helper(root)


def helper(node):
    if node is None:
        return None

    node.left = helper(node.left)
    node.right = helper(node.right)

    if node.left is None and node.right is None:
        if node.val == 0:
            return None

    return node