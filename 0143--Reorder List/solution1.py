# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        li = []

        node = head
        while node:
            li.append(node.val)
            node = node.next

        left = 0
        right = len(li) - 1

        flag = True
        node = head

        while left <= right:
            if flag:
                node.val = li[left]
                left += 1
            else:
                node.val = li[right]
                right -= 1
            flag = not flag
            node = node.next