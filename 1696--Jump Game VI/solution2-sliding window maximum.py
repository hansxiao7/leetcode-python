class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # sliding window maximum
        dp = [-sys.maxint] * len(nums)
        dp[0] = nums[0]

        deque = collections.deque()
        deque.append((dp[0], 0))

        for i in range(1, len(nums)):
            # maintain the left
            while len(deque) != 0 and i - deque[0][1] > k:
                deque.popleft()

            # update result
            dp[i] = deque[0][0] + nums[i]

            # main the right
            while len(deque) != 0 and deque[-1][0] < dp[i]:
                deque.pop()

            deque.append((dp[i], i))

        return dp[len(nums) - 1]