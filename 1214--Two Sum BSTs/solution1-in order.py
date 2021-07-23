# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        li1 = []
        li2 = []

        inorder(root1, li1)
        inorder(root2, li2)

        left = 0
        right = len(li2) - 1

        while left < len(li1) and right > -1:
            if li1[left] + li2[right] > target:
                right -= 1
            elif li1[left] + li2[right] < target:
                left += 1
            else:
                return True

        return False


def inorder(node, li):
    if node:
        inorder(node.left, li)
        li.append(node.val)
        inorder(node.right, li)