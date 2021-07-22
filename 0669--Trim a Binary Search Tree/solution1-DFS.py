# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        root = DFS_low(root, low)
        root = DFS_high(root, high)

        return root


def DFS_low(node, low):
    if node is None:
        return None

    if node.val >= low:
        node.left = DFS_low(node.left, low)
    if node.val < low:
        if node.right:
            node = node.right
            node = DFS_low(node, low)
        else:
            return None

    return node


def DFS_high(node, high):
    if node is None:
        return None

    if node.val <= high:
        node.right = DFS_high(node.right, high)
    else:
        if node.left:
            node = DFS_high(node.left, high)
        else:
            return None

    return node