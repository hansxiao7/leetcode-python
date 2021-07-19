# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Solve it with recursion
        return helper(root, p, q)


def helper(node, p, q):
    if node == p or node == q:
        return node

    if p.val < node.val and q.val < node.val:  # all in the left tree
        return helper(node.left, p, q)

    elif p.val > node.val and q.val > node.val:
        return helper(node.right, p, q)

    else:
        return node
