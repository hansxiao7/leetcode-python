# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        dp1, p1 = find_parent(root, x, 0)
        dp2, p2 = find_parent(root, y, 0)

        if p1 == p2:
            return False

        if dp1 == dp2:
            return True

        return False


def find_parent(node, x, d):
    if node.left is None and node.right is None:
        return None, None
    l = None
    r = None
    if node.left:
        if node.left.val == x:
            return d, node
        else:
            dl, l = find_parent(node.left, x, d + 1)

    if node.right:
        if node.right.val == x:
            return d, node
        else:
            dr, r = find_parent(node.right, x, d + 1)

    if l:
        return dl, l
    if r:
        return dr, r

    return None, None