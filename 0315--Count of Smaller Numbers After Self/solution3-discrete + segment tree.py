class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end

        self.left = None
        self.right = None

        self.sum = 0


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # segment Tree
        maps = {}
        temp = list(nums)

        temp = list(set(tuple(temp)))
        temp.sort()

        buckets = [0] * len(temp)

        rank = 0
        for val in temp:
            maps[val] = rank
            rank += 1

        def buildTree(left, right):
            if left > right:
                return None

            node = TreeNode(left, right)
            if left == right:
                node.sum = buckets[left]
                return node

            mid = (left + right) // 2
            node.left = buildTree(left, mid)
            node.right = buildTree(mid + 1, right)

            node.sum = node.left.sum + node.right.sum

            return node

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

        def updateTree(node, val):
            index = maps[val]

            if node.start == index and node.end == index:
                node.sum += 1
                return

            l = node.start
            r = node.end

            mid = (l + r) // 2

            if index > mid:
                updateTree(node.right, val)
            else:
                updateTree(node.left, val)

            node.sum = node.left.sum + node.right.sum

        result = [0] * len(nums)
        root = buildTree(0, len(maps.keys()) - 1)

        for i in range(len(nums) - 1, -1, -1):
            updateTree(root, nums[i])
            result[i] = rangeSum(root, 0, maps[nums[i]] - 1)

        return result