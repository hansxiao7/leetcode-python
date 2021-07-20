# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        return merge(root1, root2)


def merge(node1, node2):
    if node1 is None and node2 is None:
        return None

    if node1 is not None and node2 is None:
        return node1
    elif node1 is None and node2 is not None:
        return node2
    else:
        node = TreeNode(val=node1.val + node2.val)

    node.left = merge(node1.left, node2.left)
    node.right = merge(node1.right, node2.right)

    return node