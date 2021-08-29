# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """

        def helper(node):
            if node is None:
                return None

            node.left = helper(node.left)
            node.right = helper(node.right)

            if node.left is None and node.right is None and node.val == target:
                return None

            return node

        return helper(root)