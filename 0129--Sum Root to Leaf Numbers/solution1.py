# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS
        if root is None:
            return 0

        self.result = 0

        def helper(node, curr_val):
            if node.left is None and node.right is None:
                self.result += curr_val * 10 + node.val
                return

            if node.left:
                helper(node.left, curr_val * 10 + node.val)

            if node.right:
                helper(node.right, curr_val * 10 + node.val)

        helper(root, 0)
        return self.result