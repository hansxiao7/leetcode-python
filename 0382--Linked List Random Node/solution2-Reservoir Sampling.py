# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head

    def getRandom(self):
        """
        :rtype: int
        """
        count = 1
        node = self.head
        res = node.val

        while node is not None:
            rand = random.random()
            if rand < 1. / count:
                res = node.val

            node = node.next
            count += 1

        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()