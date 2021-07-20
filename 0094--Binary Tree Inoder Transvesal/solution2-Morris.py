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
        node = root
        while node:
            if node.left is None:
                result.append(node.val)
                node = node.right

            else:
                p = predecessor(node)
                if p.right is None:
                    p.right = node
                    node = node.left
                else:
                    p.right = None
                    result.append(node.val)
                    node = node.right

        return result


def predecessor(node):
    l = node.left

    while l.right and l.right.val != node.val:
        l = l.right

    return l

