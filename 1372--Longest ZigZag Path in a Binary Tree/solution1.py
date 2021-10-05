# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def helper(node, curr, flag):
            if node is None:
                self.res = max(self.res, curr)
                return

            if flag == 0:
                helper(node.left, curr + 1, 1)
                helper(node.right, curr + 1, 2)
            elif flag == 1:
                helper(node.left, 0, 1)
                helper(node.right, curr + 1, 2)
            elif flag == 2:
                helper(node.left, curr + 1, 1)
                helper(node.right, 0, 2)

        helper(root, -1, 0)

        return self.res