# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


def helper(p_li, p_left, p_right, in_li, in_left, in_right):
    if p_left == p_right:
        return TreeNode(val=p_li[p_left])

    if p_left > p_right:
        return None

    root_val = p_li[p_left]
    node = TreeNode(val=root_val)

    for i in range(in_left, in_right + 1):
        if in_li[i] == root_val:
            mid = i
            break

    l_in_left = in_left
    l_in_right = mid - 1

    l_p_left = p_left + 1
    l_p_right = l_p_left + mid - in_left - 1

    r_in_left = mid + 1
    r_in_right = in_right

    r_p_left = l_p_right + 1
    r_p_right = p_right

    node.left = helper(p_li, l_p_left, l_p_right, in_li, l_in_left, l_in_right)
    node.right = helper(p_li, r_p_left, r_p_right, in_li, r_in_left, r_in_right)

    return node
