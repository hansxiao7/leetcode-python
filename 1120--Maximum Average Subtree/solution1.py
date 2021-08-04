# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.result = 0

        def helper(node):
            if node is None:
                return 0, 0  # node_n, total_val

            l, l_val = helper(node.left)
            r, r_val = helper(node.right)

            avg = (node.val + l_val + r_val) / (1. + l + r)
            self.result = max(self.result, avg)

            return 1 + l + r, node.val + l_val + r_val

        helper(root)

        return self.result