# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(val=-sys.maxint)
        dummy.next = head
        node = head
        prev = dummy
        while node:
            if node.val < prev.val:
                temp = node
                prev.next = node.next

                h = dummy
                while h.next.val < temp.val:
                    h = h.next

                temp.next = h.next
                h.next = temp
            else:
                prev = node
            node = prev.next

        return dummy.next