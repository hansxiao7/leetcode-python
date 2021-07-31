# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0

        def sum_subtree(node):
            if node is None:
                return 0

            l_sum = sum_subtree(node.left)
            r_sum = sum_subtree(node.right)

            self.result += abs(l_sum - r_sum)

            return node.val + l_sum + r_sum

        sum_subtree(root)

        return self.result
