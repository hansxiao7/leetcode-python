class TrieNode:
    def __init__(self):
        self.children = [None] * 2


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        head = TrieNode()
        for num in nums:
            node = head
            for i in range(31, -1, -1):
                if num & 1 << i == 1 << i:
                    if node.children[1] is None:
                        node.children[1] = TrieNode()
                    node = node.children[1]
                else:
                    if node.children[0] is None:
                        node.children[0] = TrieNode()
                    node = node.children[0]

        cache = {}

        def helper(left, right, level):
            if (left, right) in cache:
                return cache[(left, right, level)]
            if left is None or right is None:
                return 0
            if level < 0:
                return 0

            res = 0
            flag = True
            if left.children[1] and right.children[0]:
                res = max(res, (1 << level) + helper(left.children[1], right.children[0], level - 1))
                flag = False
            if left.children[0] and right.children[1]:
                res = max(res, (1 << level) + helper(left.children[0], right.children[1], level - 1))
                flag = False

            if flag:
                res = max(res, helper(left.children[0], right.children[0], level - 1))
                res = max(res, helper(left.children[1], right.children[1], level - 1))

            cache[(left, right)] = res

            return res

        return helper(head, head, 31)