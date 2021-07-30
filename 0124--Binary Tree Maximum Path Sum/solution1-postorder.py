# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = -sys.maxint

        def postorder(node):
            if node is None:
                return 0

            l_sum = postorder(node.left)
            r_sum = postorder(node.right)

            l_sum = max(0, l_sum)
            r_sum = max(0, r_sum)

            self.result = max(self.result, node.val + l_sum + r_sum, l_sum + node.val, r_sum + node.val)

            return max(l_sum + node.val, r_sum + node.val)

        postorder(root)

        return self.result