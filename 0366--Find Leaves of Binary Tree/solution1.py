# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = {}

        def helper(node):
            if node is None:
                return 0

            l = helper(node.left)
            r = helper(node.right)

            d = max(l, r) + 1

            if d not in result:
                result[d] = []
            result[d].append(node.val)

            return d

        helper(root)
        key_li = result.keys()
        key_li.sort()

        temp = []
        for key in key_li:
            temp.append(result[key])

        return temp