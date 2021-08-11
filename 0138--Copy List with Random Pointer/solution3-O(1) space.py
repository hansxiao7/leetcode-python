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

        new_head = None

        node = head
        while node:
            new_node = Node(node.val)

            if new_head is None:
                new_head = new_node

            new_node.next = node.next
            node.next = new_node
            node = new_node.next

        node = head
        while node:
            new_node = node.next
            if node.random:
                new_node.random = node.random.next
            node = new_node.next

        # break the connection
        node = head
        while node:
            new_node = node.next
            node.next = new_node.next
            if node.next:
                new_node.next = node.next.next

            node = node.next

        return new_head

