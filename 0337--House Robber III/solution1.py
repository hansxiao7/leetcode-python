# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rob, not_rob = helper(root)
        return max(rob, not_rob)


def helper(node):
    if node is None:
        return 0, 0

    l_rob, l_not_rob = helper(node.left)
    r_rob, r_not_rob = helper(node.right)

    rob = l_not_rob + r_not_rob + node.val
    not_rob = max(l_not_rob + r_rob, l_rob + r_not_rob, l_rob + r_rob, l_not_rob + r_not_rob)

    return rob, not_rob