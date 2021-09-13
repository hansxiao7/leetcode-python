class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        self.res = sys.maxint

        workers = [0] * k

        def helper(pos, currMax):
            if currMax >= self.res:
                return
            if pos == len(jobs):
                self.res = min(self.res, currMax)
                return

            for i in range(k):
                if i != 0 and workers[i] == workers[i - 1]: continue
                workers[i] += jobs[pos]
                currMax = max(workers)
                helper(pos + 1, currMax)
                workers[i] -= jobs[pos]

        helper(0, 0)
        return self.res