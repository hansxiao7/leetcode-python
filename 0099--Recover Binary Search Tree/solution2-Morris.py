# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        node = root
        last = None
        start = False

        while node:
            if node.left is None:
                last = node
                node = node.right
            else:
                p = predecessor(node)

                if p.right is None:
                    p.right = node
                    node = node.left
                elif p.right == node:
                    p.right = None
                    last = node
                    node = node.right
            if node and last:
                if last.val > node.val:
                    if start == False:
                        start = True
                        x = last
                    y = node

        x.val, y.val = y.val, x.val


def predecessor(node):
    p = node.left

    while p.right and p.right != node:
        p = p.right

    return p