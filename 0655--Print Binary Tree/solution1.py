# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        def findHeight(node):
            if node is None:
                return 0

            l = findHeight(node.left)
            r = findHeight(node.right)

            return max(l, r) + 1

        height = findHeight(root)
        col = 2 ** height - 1

        res = [['' for _ in range(col)] for _ in range(height)]

        pos = col // 2

        def helper(node, pos, h):
            if node is None:
                return

            res[h][pos] = str(node.val)
            helper(node.left, pos - 2 ** (height - h - 2), h + 1)
            helper(node.right, pos + 2 ** (height - h - 2), h + 1)

        helper(root, pos, 0)
        return res