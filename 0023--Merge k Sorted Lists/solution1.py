# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]
        prev = None
        k = len(lists)
        heap = []

        for i in range(k):
            if lists[i]:
                heap.append((lists[i].val, lists[i]))

        start = None
        heapq.heapify(heap)
        while len(heap) != 0:
            val, node = heapq.heappop(heap)

            if prev is None:
                start = node
            else:
                prev.next = node

            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))

            prev = node

        return start