# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return dfs(l1, l2, 0)


def dfs(n1, n2, r):
    if n1 is None and n2 is None:
        if r > 0:
            return ListNode(val=r)
        return None

    if n1 is None and n2:
        temp = n2.val + r
        node = ListNode(val=temp % 10)
        r = temp // 10
        node.next = dfs(n1, n2.next, r)
    elif n1 and n2 is None:
        temp = n1.val + r
        node = ListNode(val=temp % 10)
        r = temp // 10
        node.next = dfs(n1.next, n2, r)
    else:
        temp = n1.val + n2.val + r
        node = ListNode(val=temp % 10)
        r = temp // 10
        node.next = dfs(n1.next, n2.next, r)

    return node