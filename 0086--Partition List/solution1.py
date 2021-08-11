# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        temp1 = []
        temp2 = []

        node = head

        while node:
            if node.val >= x:
                temp1.append(node)
            else:
                temp2.append(node)
            temp = node.next
            node.next = None
            node = temp
        temp1.append(None)
        temp2.append(None)
        new_head = None
        for i in range(len(temp2) - 1):
            if new_head is None:
                new_head = temp2[i]
            temp2[i].next = temp2[i + 1]

        if new_head is not None:
            end = temp2[-2]
        else:
            end = None
        for i in range(len(temp1) - 1):
            if i == 0:
                if new_head is None:
                    new_head = temp1[i]
                if end is not None:
                    end.next = temp1[i]

            temp1[i].next = temp1[i + 1]

        return new_head

