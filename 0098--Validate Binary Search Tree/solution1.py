# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        _, _, result = helper(root)

        return result


def helper(node):
    if node is None:
        return -sys.maxint, sys.maxint, True  # max, min, T/F

    lmax, lmin, l = helper(node.left)
    rmax, rmin, r = helper(node.right)

    if node.val > lmax and node.val < rmin:
        temp = True
    else:
        temp = False

    nmax = max(rmax, node.val)
    nmin = min(lmin, node.val)

    return nmax, nmin, temp and l and r
