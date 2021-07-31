# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        dfs(root, targetSum, [], result)

        return result


def dfs(node, k, t, result):
    if node is None:
        return
    if node.left is None and node.right is None:
        if k - node.val != 0:
            return
        if k == node.val:
            t.append(node.val)
            result.append(t)
            return

    if node.left:
        dfs(node.left, k - node.val, t + [node.val], result)
    if node.right:
        dfs(node.right, k - node.val, t + [node.val], result)
