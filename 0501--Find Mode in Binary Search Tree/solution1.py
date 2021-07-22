# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dict1 = {}
        inorder(root, dict1)

        result = []
        max_n = 0
        print(dict1)
        for key in dict1.keys():
            if dict1[key] == max_n:
                result.append(key)
            elif dict1[key] > max_n:
                result = [key]
                max_n = dict1[key]

        return result


def inorder(node, dict1):
    if node:
        inorder(node.left, dict1)
        dict1[node.val] = dict1.get(node.val, 0) + 1
        inorder(node.right, dict1)