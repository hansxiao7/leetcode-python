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
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            if root.val == targetSum:
                return 1
            else:
                return 0

        dict1 = {0: 1}
        curr_sum = 0
        return prefix_sum(root, dict1, curr_sum, targetSum)


def prefix_sum(node, dict1, curr_sum, target):
    if node is None:
        return 0

    result = 0
    curr_sum += node.val

    result += dict1.get(curr_sum - target, 0)
    dict1[curr_sum] = dict1.get(curr_sum, 0) + 1

    result += prefix_sum(node.left, dict1, curr_sum, target)
    result += prefix_sum(node.right, dict1, curr_sum, target)

    dict1[curr_sum] -= 1

    return result