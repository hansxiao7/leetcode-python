# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        counts = {}

        def helper(node):
            if node is None:
                return 0

            l = helper(node.left)
            r = helper(node.right)

            counts[l + r + node.val] = counts.get(l + r + node.val, 0) + 1

            return l + r + node.val

        helper(root)

        result = []
        maxCount = 0

        for key in counts.keys():
            if counts[key] > maxCount:
                maxCount = counts[key]
                result = [key]
            elif counts[key] == maxCount:
                result.append(key)

        return result