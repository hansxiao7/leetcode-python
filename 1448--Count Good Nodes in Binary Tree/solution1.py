# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0

        # dfs
        def helper(node, prev_max):
            if node is None:
                return None

            if node.val >= prev_max:
                prev_max = node.val
                self.result += 1
            helper(node.left, prev_max)
            helper(node.right, prev_max)

        helper(root, -sys.maxint)
        return self.result