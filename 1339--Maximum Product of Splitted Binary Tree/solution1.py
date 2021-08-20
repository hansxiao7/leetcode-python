# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0

        def helper(node, total):
            if node is None:
                return 0

            l = helper(node.left, total)
            r = helper(node.right, total)

            curr = node.val + l + r

            self.result = max(self.result, curr * (total - curr))

            return curr

        total = helper(root, 0)
        self.result = 0
        helper(root, total)

        return self.result % (10 ** 9 + 7)