# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        root = helper(root)
        return root


def helper(node):
    if node is None:
        return None

    temp = node.right
    node.right = helper(node.left)
    node.left = helper(temp)

    return node