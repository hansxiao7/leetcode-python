# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0

        def helper(node):
            if node is None:
                return 0

            l = helper(node.left)
            r = helper(node.right)

            if node.left and node.right:
                if node.left.val == node.right.val == node.val:
                    self.result = max(self.result, l + r + 1)

            if node.left:
                if node.val == node.left.val:
                    l += 1
                else:
                    l = 1
            if node.right:
                if node.val == node.right.val:
                    r += 1
                else:
                    r = 1

            self.result = max(self.result, l, r)

            return max(1, l, r)

        helper(root)
        if self.result > 1:
            return self.result - 1
        else:
            return 0