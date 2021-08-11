# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def merge(p1, p2):
            if p1 is None:
                return p2
            if p2 is None:
                return p1

            dummy = ListNode()
            prev = dummy

            while p1 and p2:
                if p1.val <= p2.val:
                    prev.next = p1
                    prev = p1
                    p1 = p1.next
                else:
                    prev.next = p2
                    prev = p2
                    p2 = p2.next

            if p1:
                prev.next = p1
            if p2:
                prev.next = p2

            return dummy.next

        def merge_sort(head):
            if head is None or head.next is None:
                return head
            p1 = head
            p2 = head

            while p2 and p2.next:
                prev = p1
                p1 = p1.next
                p2 = p2.next.next

            prev.next = None

            n1 = merge_sort(head)
            n2 = merge_sort(p1)

            return merge(n1, n2)

        return merge_sort(head)

