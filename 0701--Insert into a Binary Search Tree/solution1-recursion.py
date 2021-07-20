# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        return helper(root, val)


def helper(node, val):
    if node is None:
        node = TreeNode(val=val)

    if val > node.val:
        node.right = helper(node.right, val)

    elif val < node.val:
        node.left = helper(node.left, val)

    return node