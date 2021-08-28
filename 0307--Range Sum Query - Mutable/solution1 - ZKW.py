class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.result = [0] * 2 * n
        for i in range(n, 2 * n):
            self.result[i] = nums[i - n]

        for i in range(n - 1, -1, -1):
            self.result[i] = self.result[2 * i] + self.result[2 * i + 1]

        self.n = n

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        i = index + self.n
        diff = val - self.result[i]

        while i >= 0:
            self.result[i] += diff
            if i == 0:
                break
            i = i // 2

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        res = 0

        i = left + self.n
        j = right + self.n

        while i <= j:
            if i % 2 == 1:
                res += self.result[i]
                i += 1
            if j % 2 == 0:
                res += self.result[j]
                j -= 1

            i = i // 2
            j = j // 2

            if i == j:
                res += self.result[i]
                break

        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)