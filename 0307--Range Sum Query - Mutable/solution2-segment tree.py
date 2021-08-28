class TreeNode:
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.sum = 0

        self.start = start
        self.end = end


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        def buildTree(left, right):
            if left > right:
                return None

            node = TreeNode(left, right)
            if left == right:
                node.sum = nums[left]
                return node

            mid = (left + right) // 2

            node.left = buildTree(left, mid)
            node.right = buildTree(mid + 1, right)

            node.sum = node.left.sum + node.right.sum

            return node

        self.root = buildTree(0, len(nums) - 1)

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """

        def updateTree(node, index, val):
            if node.start == node.end and node.end == index:
                node.sum = val
                return

            l = node.start
            r = node.end

            mid = (l + r) // 2

            if index <= mid:
                updateTree(node.left, index, val)
            else:
                updateTree(node.right, index, val)

            node.sum = node.left.sum + node.right.sum

        updateTree(self.root, index, val)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        def rangeSum(node, left, right):
            if left > right:
                return 0

            l = node.start
            r = node.end

            if l == left and r == right:
                return node.sum

            mid = (l + r) // 2
            if left > mid:
                return rangeSum(node.right, left, right)
            elif right <= mid:
                return rangeSum(node.left, left, right)
            else:
                return rangeSum(node.left, left, mid) + rangeSum(node.right, mid + 1, right)

        return rangeSum(self.root, left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)