# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return helper(1, n)


def helper(left, right):
    if left == right:
        node = TreeNode(val=left)
        return [node]
    if left > right:
        return [None]

    result = []

    for curr in range(left, right + 1):
        left_li = helper(left, curr - 1)
        right_li = helper(curr + 1, right)
        for i in range(len(left_li)):
            for j in range(len(right_li)):
                node = TreeNode(val=curr)
                node.left = left_li[i]
                node.right = right_li[j]
                result.append(node)

    return result