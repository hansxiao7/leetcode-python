# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        stackLeft = []
        stackRight = []

        def pushAllLeft(node):
            if node:
                while node:
                    stackLeft.append(node)
                    node = node.left

        def pushAllRight(node):
            if node:
                while node:
                    stackRight.append(node)
                    node = node.right

        def popLeft():
            node = stackLeft.pop()
            pushAllLeft(node.right)

        def popRight():
            node = stackRight.pop()
            pushAllRight(node.left)

        pushAllLeft(root)
        pushAllRight(root)

        while len(stackLeft) != 0 and len(stackRight) != 0 and stackLeft[-1] != stackRight[-1]:
            l = stackLeft[-1]
            r = stackRight[-1]

            if l.val + r.val < k:
                popLeft()
            elif l.val + r.val > k:
                popRight()
            else:
                return True

        return False
