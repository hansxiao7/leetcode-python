# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        inorder(result, root)
        return result


def inorder(result, node):
    if node is not None:
        inorder(result, node.left)
        result.append(node.val)
        inorder(result, node.right)

