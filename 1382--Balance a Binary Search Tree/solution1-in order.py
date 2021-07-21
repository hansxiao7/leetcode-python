# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        li = []
        in_order(li, root)

        return helper(li, 0, len(li) - 1)


def in_order(li, node):
    if node:
        in_order(li, node.left)
        li.append(node)
        in_order(li, node.right)


def helper(li, left, right):
    if left < right:
        mid = (left + right) // 2
        li[mid].left = helper(li, left, mid - 1)
        li[mid].right = helper(li, mid + 1, right)
        return li[mid]
    elif left == right:
        li[left].left = li[left].right = None
        return li[left]
    else:
        return None
