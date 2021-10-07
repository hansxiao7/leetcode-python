# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head

        maps = {0: dummy}
        deleted = set()
        node = head
        tempSum = 0
        while node:

            tempSum += node.val
            if tempSum in maps and maps[tempSum] not in deleted:
                prev = maps[tempSum]

                temp = prev.next
                while temp != node.next:
                    deleted.add(temp)
                    temp = temp.next
                node = node.next
                prev.next = node
                continue

            maps[tempSum] = node
            node = node.next

        return dummy.next
