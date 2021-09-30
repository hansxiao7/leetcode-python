class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0
        res = None
        for i in range(len(self.nums)):
            if self.nums[i] != target:
                continue

            count += 1
            rand = random.random()
            if rand < 1. / count:
                res = i

        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)