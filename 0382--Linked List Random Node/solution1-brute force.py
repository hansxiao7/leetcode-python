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
        self.li = []
        node = head

        while node:
            self.li.append(node.val)
            node = node.next

    def getRandom(self):
        """
        :rtype: int
        """
        n = len(self.li)

        rand = random.randrange(0, n)
        return self.li[rand]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()