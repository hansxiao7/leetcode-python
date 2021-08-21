class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # prefix + binary search
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        queue = collections.deque()
        result = sys.maxint
        queue.append(-1)

        for i in range(len(nums) + 1):
            while len(queue) != 0 and prefix[i] - prefix[queue[0]] >= k:
                result = min(result, i - queue[0])
                queue.popleft()

            while len(queue) != 0 and prefix[i] <= prefix[queue[-1]]:
                queue.pop()

            queue.append(i)

        if result == sys.maxint:
            return -1
        return result