class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end

        self.left = None
        self.right = None

        self.sum = 0


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # discrete
        maps = {}

        temp = set()
        for num in nums:
            temp.add(2 * num)
            temp.add(num)
        temp = list(temp)
        temp.sort()

        for i in range(len(temp)):
            maps[temp[i]] = i

        # define segment tree functions
        def buildTree(left, right):
            if left > right:
                return None

            node = TreeNode(left, right)
            if left == right:
                return node

            mid = (left + right) // 2

            node.left = buildTree(left, mid)
            node.right = buildTree(mid + 1, right)

            # node.sum = node.left.sum + node.right.sum

            return node

        def update(node, val):
            index = maps[val]

            if node.start == index and node.end == index:
                node.sum += 1
                return

            l = node.start
            r = node.end

            mid = (l + r) // 2

            if index <= mid:
                update(node.left, val)
            elif index > mid:
                update(node.right, val)

            node.sum = node.left.sum + node.right.sum

        def rangeSum(node, left, right):
            if left > right:
                return 0

            if node.start == left and node.end == right:
                return node.sum

            l = node.start
            r = node.end
            mid = (l + r) // 2

            if left > mid:
                return rangeSum(node.right, left, right)
            elif right <= mid:
                return rangeSum(node.left, left, right)
            else:
                return rangeSum(node.left, left, mid) + rangeSum(node.right, mid + 1, right)

        maxKey = max(maps.values())
        root = buildTree(0, maxKey)

        result = 0

        for num in nums:
            result += rangeSum(root, 0, maxKey) - rangeSum(root, 0, maps[2 * num])
            update(root, num)

        return result
