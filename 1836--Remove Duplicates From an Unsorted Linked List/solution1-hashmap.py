# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        counts = {}
        key_li = []

        node = head
        while node:
            key_li.append(node.val)
            if node.val not in counts:
                counts[node.val] = []
            counts[node.val].append(node)
            node = node.next

        dummy = ListNode()
        tail = dummy

        for key in key_li:
            if len(counts[key]) > 1:
                continue
            tail.next = counts[key][0]
            counts[key][0].next = None
            tail = tail.next

        return dummy.next