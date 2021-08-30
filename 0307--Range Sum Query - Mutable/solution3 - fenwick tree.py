class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        tree = [0] * (len(nums) + 1)

        for index in range(len(nums)):
            i = index + 1

            while i < len(tree):
                tree[i] += nums[index]
                i += lowbit(i)

        self.tree = tree
        self.nums = nums

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        i = index + 1
        diff = val - self.nums[index]
        self.nums[index] = val
        while i < len(self.tree):
            self.tree[i] += diff
            i += lowbit(i)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        def query(index):
            i = index + 1
            total = 0
            while i > 0:
                total += self.tree[i]
                i -= lowbit(i)

            return total

        return query(right) - query(left - 1)


def lowbit(x):
    return x & (-x)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)