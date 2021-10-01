class TrieNode:
    def __init__(self):
        self.children = [None] * 2


class Solution(object):
    def maximizeXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        head = TrieNode()

        def addNum(num):
            node = head
            for i in range(31, -1, -1):
                if num & (1 << i) != 0:
                    if node.children[1] is None:
                        node.children[1] = TrieNode()
                    node = node.children[1]
                else:
                    if node.children[0] is None:
                        node.children[0] = TrieNode()
                    node = node.children[0]

        def helper(head, num):
            res = 0

            node = head
            level = 31
            while level >= 0:
                if num & (1 << level) != 0:
                    # go to 1
                    if node.children[0]:
                        res += 1 << level
                        node = node.children[0]
                    elif node.children[1]:
                        node = node.children[1]
                    else:
                        return -1
                else:
                    if node.children[1]:
                        res += 1 << level
                        node = node.children[1]
                    elif node.children[0]:
                        node = node.children[0]
                    else:
                        return -1

                level -= 1
            return res

        result = [-1] * len(queries)
        original_pos = {}
        for i in range(len(queries)):
            if tuple(queries[i]) not in original_pos:
                original_pos[tuple(queries[i])] = []
            original_pos[tuple(queries[i])].append(i)

        # offline queries; sort first
        nums = list(set(tuple(nums)))
        nums.sort()
        queries.sort(key=lambda x: (x[1], x[0]))

        pos = 0
        visited = set()
        for num, bar in queries:
            if (num, bar) in visited:
                continue
            while pos < len(nums) and nums[pos] <= bar:
                addNum(nums[pos])
                pos += 1

            res = helper(head, num)
            for oPos in original_pos[(num, bar)]:
                result[oPos] = res
            visited.add((num, bar))
        return result