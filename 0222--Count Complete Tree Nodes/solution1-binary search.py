# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # calculate the depth
        node = root
        if root is None:
            return 0

        d = 0
        while node:
            d += 1
            node = node.left

        result = 0
        # calculate the full amount
        for i in range(d - 1):
            result += 2 ** i

        left = 0
        right = 2 ** (d - 1) - 1

        while left < right:
            mid = (left + right) // 2
            temp = check_node(root, mid, 0, 2 ** (d - 1) - 1, d - 1)
            if temp is None:
                right = mid
            else:
                left = mid + 1

        temp = check_node(root, left, 0, 2 ** (d - 1) - 1, d - 1)
        if temp == None:
            result += left
        else:
            result += left + 1
        return result


def check_node(node, pivot, left, right, k):
    if k == 0:
        return node

    if left < right:
        mid = (left + right) // 2

        if pivot <= mid:
            return check_node(node.left, pivot, left, mid, k - 1)
        elif pivot > mid:
            return check_node(node.right, pivot, mid + 1, right, k - 1)