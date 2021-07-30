# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_n, curr_n = helper(root)

        return max_n


def helper(node):
    if node.left is None and node.right is None:
        return 1, 1

    curr_n = 0
    max_n = 0

    if node.left:
        max_l, curr_l = helper(node.left)

        if node.left.val == node.val + 1:
            curr_n = 1 + curr_l
        else:
            curr_n = 1
        max_n = max(curr_n, max_l)

    if node.right:
        max_r, curr_r = helper(node.right)

        if node.right.val == node.val + 1:
            curr_n = max(curr_n, 1 + curr_r)
        else:
            curr_n = max(curr_n, 1)
        max_n = max(max_n, max_r, curr_n)
    return max_n, curr_n