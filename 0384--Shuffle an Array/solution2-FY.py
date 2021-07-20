class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = [i for i in nums]
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.nums)):
            rand_id = random.randrange(len(self.nums))
            self.nums[i], self.nums[rand_id] = self.nums[rand_id], self.nums[i]

        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()