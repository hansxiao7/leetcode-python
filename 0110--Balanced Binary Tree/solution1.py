# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        _, result = helper(root)
        return result


def helper(node):
    if node is None:
        return 0, True

    l, l_check = helper(node.left)
    r, r_check = helper(node.right)

    if l_check and r_check and abs(l - r) <= 1:
        return max(l, r) + 1, True
    else:
        return max(l, r) + 1, False
