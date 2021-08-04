# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def flatten(node):
            if node is None:
                return None, None

            lstart, lend = flatten(node.left)
            rstart, rend = flatten(node.right)

            node.left = None

            start = node
            end = node
            if lstart:
                start.right = lstart
                end = lend
            if rstart:
                end.right = rstart
                end = rend

            return start, end

        root, _ = flatten(root)
        return root