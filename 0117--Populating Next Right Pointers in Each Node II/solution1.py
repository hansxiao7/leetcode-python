"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        leftmost = root

        while leftmost.left or leftmost.right:
            head = leftmost
            flag = 0

            while head:
                if (head.left or head.right) and flag == 0:
                    if head.right:
                        if head.right.left or head.right.right:
                            leftmost = head.right
                            flag = 1
                    if head.left:
                        if head.left.left or head.left.right:
                            leftmost = head.left
                            flag = 1

                if head.left and head.right:
                    head.left.next = head.right

                head2 = head.next

                while head2:
                    if head2.left or head2.right:
                        break
                    head2 = head2.next

                if head2:
                    if head.right:
                        if head2.left:
                            head.right.next = head2.left
                        elif head2.right:
                            head.right.next = head2.right
                    elif head.left:
                        if head2.left:
                            head.left.next = head2.left
                        elif head2.right:
                            head.left.next = head2.right

                head = head2

            if flag == 0:
                break

        return root