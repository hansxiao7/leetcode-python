class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.result = []
        x = min(k, len(nums))
        for i in range(x):
            self.result.append(nums[i])

        for j in range((x - 2) // 2, -1, -1):
            sift(self.result, j, x - 1)

        for m in range(x, len(nums)):
            if nums[m] > self.result[0]:
                self.result[0] = nums[m]
                sift(self.result, 0, x - 1)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.result) < self.k:
            self.result.append(val)
            sift(self.result, 0, len(self.result) - 1)
        elif val > self.result[0]:
            self.result[0] = val
            sift(self.result, 0, len(self.result) - 1)

        return self.result[0]


def sift(li, low, high):
    i = low
    j = 2 * i + 1

    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:
            j = j + 1

        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]
            i = j
            j = 2 * i + 1
        else:
            break

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)