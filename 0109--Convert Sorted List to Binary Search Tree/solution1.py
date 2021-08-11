# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None

        li = []

        node = head
        while node:
            li.append(node.val)
            node = node.next

        def helper(li, left, right):
            if left < right:
                mid = (left + right) // 2
                node = TreeNode(val=li[mid])

                node.left = helper(li, left, mid - 1)
                node.right = helper(li, mid + 1, right)

            elif left == right:
                node = TreeNode(val=li[left])
            else:
                node = None
            return node

        return helper(li, 0, len(li) - 1)
