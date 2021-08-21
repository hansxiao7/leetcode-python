class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        def helper(k):
            result = 0
            queue = collections.deque()

            for i in range(len(arr)):
                # keep left
                while len(queue) != 0 and i - queue[0] >= k:
                    queue.popleft()

                # keep right
                while len(queue) != 0 and arr[i] <= arr[queue[-1]]:
                    queue.pop()

                queue.append(i)

                if i >= k - 1:
                    result += arr[queue[0]]

            return result % (10 ** 9 + 7)

        result = 0

        for k in range(1, len(arr) + 1):
            result += helper(k)

        return result % (10 ** 9 + 7)
