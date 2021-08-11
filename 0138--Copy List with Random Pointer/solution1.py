"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        # hashmap
        dict1 = {None: None}

        node = head
        while node:
            dict1[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            dict1[node].next = dict1[node.next]
            dict1[node].random = dict1[node.random]
            node = node.next

        return dict1[head]