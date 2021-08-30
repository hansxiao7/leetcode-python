class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end

        self.left = None
        self.right = None

        self.sum = 0


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # discrete
        # calculate prefix
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        maps = {}

        tempSet = set()

        for i in range(len(prefix)):
            tempSet.add(prefix[i])
            tempSet.add(lower + prefix[i])
            tempSet.add(upper + prefix[i])

        tempSet.add(upper)
        tempSet.add(lower)
        tempSet = list(tempSet)
        tempSet.sort()

        rank = 0
        for i in range(len(tempSet)):
            maps[tempSet[i]] = rank
            rank += 1

        def buildTree(left, right):
            if left > right:
                return None

            node = TreeNode(left, right)
            if left == right:
                return node

            mid = (left + right) // 2
            node.left = buildTree(left, mid)
            node.right = buildTree(mid + 1, right)

            node.sum = node.left.sum + node.right.sum

            return node

        def update(node, val):
            index = maps[val]

            if node.start == index and node.end == index:
                node.sum += 1
                return

            l = node.start
            r = node.end

            mid = (l + r) // 2

            if index > mid:
                update(node.right, val)
            else:
                update(node.left, val)

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

        root = buildTree(0, rank - 1)
        total = prefix[-1]
        update(root, total)

        res = 0

        for i in range(len(prefix) - 2, -1, -1):
            left = maps[prefix[i] + lower]
            right = maps[prefix[i] + upper]
            res += rangeSum(root, left, right)

            update(root, prefix[i])

        left = maps[lower]
        right = maps[upper]
        res += rangeSum(root, left, right)

        return res



