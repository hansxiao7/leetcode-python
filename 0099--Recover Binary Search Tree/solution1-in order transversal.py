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
        li = []
        build_li(li, root)

        for i in range(len(li) - 1):
            if li[i].val < li[i + 1].val:
                continue
            else:
                temp = i
                for j in range(i + 1, len(li)):
                    if li[j].val < li[temp].val:
                        temp = j
                li[temp].val, li[i].val = li[i].val, li[temp].val
                break


def build_li(result, node):
    if node:
        build_li(result, node.left)
        result.append(node)
        build_li(result, node.right)

