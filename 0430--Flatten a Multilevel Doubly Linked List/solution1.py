"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        helper(head)

        return head


def helper(node):
    while node.next and node.child is None:
        node = node.next

    end = node
    if node.child:
        temp = node.next
        node.next = node.child
        node.child.prev = node
        end = helper(node.child)
        node.child = None

        end.next = temp
        if temp:
            temp.prev = end
            end = helper(temp)

    return end