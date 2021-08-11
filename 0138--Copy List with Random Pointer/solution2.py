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
        dict1 = {}
        dummy = Node(0)
        tail = dummy

        node = head
        while node:
            if node not in dict1:
                new_node = Node(node.val)
                dict1[node] = new_node
            else:
                new_node = dict1[node]

            if node.next:
                if node.next in dict1:
                    next_node = dict1[node.next]
                else:
                    next_node = Node(node.next.val)
                    dict1[node.next] = next_node
                new_node.next = next_node

            if node.random:
                if node.random in dict1:
                    new_r_node = dict1[node.random]
                else:
                    new_r_node = Node(node.random.val)
                    dict1[node.random] = new_r_node

                new_node.random = new_r_node

            node = node.next
            tail.next = new_node
            tail = tail.next

        return dummy.next

