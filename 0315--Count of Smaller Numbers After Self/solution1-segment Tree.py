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
        maxV = max(nums) + 10 ** 4

        # buckets = [0] * (maxV + 1)

        def buildTree(left, right):
            if left > right:
                return None

            node = TreeNode(left, right)
            if left == right:
                node.sum = 0
                return node

            mid = (left + right) // 2
            node.left = buildTree(left, mid)
            node.right = buildTree(mid + 1, right)

            node.sum = node.left.sum + node.right.sum

            return node

        def update(node, index):
            if node.start == index and node.end == index:
                node.sum += 1
                return

            l = node.start
            r = node.end

            mid = (l + r) // 2

            if index <= mid:
                update(node.left, index)
            else:
                update(node.right, index)

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

        root = buildTree(0, maxV)
        result = [0 for _ in range(len(nums))]

        for i in range(len(nums) - 1, -1, -1):
            update(root, nums[i] + 10 ** 4)
            temp = rangeSum(root, 0, nums[i] + 10 ** 4 - 1)
            result[i] = temp

        return result

