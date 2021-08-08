# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        if head.next is None:
            return True

        li = []
        node = head
        while node:
            li.append(node.val)
            node = node.next

        for i in range(len(li) // 2):
            if li[i] == li[len(li) - 1 - i]:
                continue
            else:
                return False

        return True