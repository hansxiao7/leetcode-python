# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        nmax, nmin, n_bst, n_n = check_bst(root)

        return n_n


def check_bst(node):
    if node is None:
        return -sys.maxint, sys.maxint, True, 0

    lmax, lmin, l_bst, l_n = check_bst(node.left)
    rmax, rmin, r_bst, r_n = check_bst(node.right)

    if node.val > lmax and node.val < rmin and l_bst and r_bst:  # bst
        n_bst = True
        n_n = l_n + r_n + 1

    else:
        n_bst = False
        n_n = max(l_n, r_n)

    nmin = min(lmin, node.val)
    nmax = max(rmax, node.val)

    return nmax, nmin, n_bst, n_n
