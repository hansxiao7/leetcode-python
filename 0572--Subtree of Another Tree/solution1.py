# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        return helper(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


def helper(node, subnode):
    if node == None and subnode == None:
        return True
    elif node == None or subnode == None:
        return False

    return node.val == subnode.val and helper(node.left, subnode.left) and helper(node.right, subnode.right)

