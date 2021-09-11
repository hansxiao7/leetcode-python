# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        ranks = {}
        res = []

        def helper(node):
            if node is None:
                return None

            l = helper(node.left)
            r = helper(node.right)

            subtree = (node.val, l, r)

            ranks[subtree] = ranks.get(subtree, 0) + 1

            if ranks[subtree] == 2:
                res.append(node)

            return subtree

        helper(root)
        return res