class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = collections.deque()

        result = []
        for i in range(len(nums)):
            # left
            while len(queue) != 0 and i - queue[0] >= k:
                queue.popleft()

            while len(queue) != 0 and nums[i] >= nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            if i >= k - 1:
                result.append(nums[queue[0]])

        return result