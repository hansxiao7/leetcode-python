class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        maps = {}

        for i in range(len(nums)):
            if nums[i] not in maps:
                maps[nums[i]] = []

            maps[nums[i]].append(i)

        self.maps = maps

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        li = self.maps[target]

        return li[random.randrange(0, len(li))]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)