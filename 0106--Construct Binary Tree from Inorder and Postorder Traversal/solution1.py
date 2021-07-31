# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return helper(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)


def helper(inorder, left1, right1, postorder, left2, right2):
    if left1 == right1:
        return TreeNode(val=inorder[left1])
    if left1 > right1:
        return None

    root_val = postorder[right2]
    node = TreeNode(val=root_val)

    for i in range(left1, right1 + 1):
        if inorder[i] == root_val:
            mid = i
            break

    l_left1 = left1
    l_right1 = mid - 1

    r_left1 = mid + 1
    r_right1 = right1

    l_left2 = left2
    l_right2 = l_left2 + mid - 1 - left1

    r_left2 = l_right2 + 1
    r_right2 = right2 - 1

    node.left = helper(inorder, l_left1, l_right1, postorder, l_left2, l_right2)
    node.right = helper(inorder, r_left1, r_right1, postorder, r_left2, r_right2)

    return node