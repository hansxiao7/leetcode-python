# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left is None and root.right is None:
            return False
        self.result = False

        def helper(node, target):
            if node is None:
                return 0

            l = helper(node.left, target)
            r = helper(node.right, target)

            if (node.left and l == target) or (node.right and r == target):
                self.result = True

            if l + r + node.val == target and node != root:
                self.result = True

            return l + r + node.val

        total = helper(root, sys.maxint)

        if total % 2 != 0:
            return False

        target = total // 2
        helper(root, target)

        return self.result