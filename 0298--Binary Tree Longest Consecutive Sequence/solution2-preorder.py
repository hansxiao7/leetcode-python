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

        return preorder(root, root.val, 0, 0)


def preorder(node, prev, curr_l, max_v):
    if node is None:
        return max_v

    if node.val == prev + 1:
        curr_l += 1
    else:
        curr_l = 1

    if curr_l > max_v:
        max_v = curr_l

    max_l = preorder(node.left, node.val, curr_l, max_v)
    max_r = preorder(node.right, node.val, curr_l, max_v)

    return max(max_l, max_r)