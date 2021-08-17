# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0

        def helper(node):
            if node is None:
                # max, min, check, sum
                return -sys.maxint, sys.maxint, True, 0

            lmax, lmin, l, l_v = helper(node.left)
            rmax, rmin, r, r_v = helper(node.right)

            if l and r:
                if node.val > lmax and node.val < rmin:
                    nmax = max(rmax, node.val)
                    nmin = min(lmin, node.val)
                    n = True
                    n_v = l_v + r_v + node.val
                else:
                    nmax = sys.maxint
                    nmin = -sys.maxint
                    n = False
                    n_v = max(l_v, r_v)
            else:
                n = False
                nmax = sys.maxint
                nmin = -sys.maxint

                if l:
                    n_v = l_v
                elif r:
                    n_v = r_v
                else:
                    n_v = -sys.maxint

            self.result = max(self.result, n_v)

            return nmax, nmin, n, n_v

        helper(root)
        return self.result
