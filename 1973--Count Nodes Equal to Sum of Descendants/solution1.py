# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def equalToDescendants(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.result = 0

        def helper(node):
            if node is None:
                return 0

            l = helper(node.left)
            r = helper(node.right)

            if node.val == (l + r):
                self.result += 1

            return l + r + node.val

        helper(root)
        return self.result