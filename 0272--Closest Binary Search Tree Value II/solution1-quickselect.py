# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        result = []
        inorder(result, root)
        quick_select(result, 0, len(result) - 1, k, target)

        return result[:k]


def partition(li, left, right, target):
    # random swap
    rand_id = random.randrange(left, right + 1)
    li[left], li[rand_id] = li[rand_id], li[left]

    i = left
    j = right
    temp = li[left]

    while i < j:
        while i < j and abs(target - li[j]) >= abs(target - temp):
            j -= 1
        li[i] = li[j]

        while i < j and abs(target - li[i]) < abs(target - temp):
            i += 1
        li[j] = li[i]

    li[i] = temp

    return i


def quick_select(li, left, right, k, target):
    if left < right:
        mid = partition(li, left, right, target)
        if k > mid - left + 1:
            quick_select(li, mid + 1, right, k - (mid - left + 1), target)
        elif k < mid - left + 1:
            quick_select(li, left, mid, k, target)
        else:
            return
    else:
        return


def inorder(result, node):
    if node:
        inorder(result, node.left)
        result.append(node.val)
        inorder(result, node.right)