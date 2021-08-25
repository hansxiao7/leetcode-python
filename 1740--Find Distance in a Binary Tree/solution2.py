# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDistance(self, root, p, q):
        """
        :type root: TreeNode
        :type p: int
        :type q: int
        :rtype: int
        """
        if p == q:
            return 0
        result = []

        def helper(node, curr, target):
            if node is None:
                return

            if node.val == target:
                result.append(curr)
                return

            helper(node.left, curr + 1, target)
            helper(node.right, curr + 1, target)

        helper(root.left, 1, p)
        posP = True  # left
        if len(result) == 0:
            posP = False  # right
            helper(root.right, 1, p)

        helper(root.left, 1, q)
        posQ = True
        if len(result) != 2:
            posQ = False
            helper(root.right, 1, q)

        if len(result) == 2:
            if posQ == posP:
                return abs(result[0] - result[1])
            else:
                return result[0] + result[1]

        else:
            return result[0]
