# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node):
            if node is None:
                return None, True

            lval, l = helper(node.left)
            rval, r = helper(node.right)

            if lval is None:
                lval = node.val
            if rval is None:
                rval = node.val

            n = lval == rval and lval == node.val and l and r

            return node.val, n

        _, result = helper(root)

        return result