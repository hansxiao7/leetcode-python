# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """

        node = root
        prev = None

        while node:
            if node.val > p.val:
                prev = node
                node = node.left
            elif node.val < p.val:
                node = node.right
            else:  # node.val == p.val
                p = node.right
                if p:
                    while p.left:
                        p = p.left
                    return p
                else:
                    return prev
