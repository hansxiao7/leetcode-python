class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        queue = [('0000', 0)]
        deadSet = set(tuple(deadends))
        if '0000' in deadSet:
            return -1
        minDis = [sys.maxint] * 10000
        minDis[0] = 0
        t = int(target)

        while len(queue) != 0:
            curr, dis = queue.pop(0)

            for i in range(4):
                child1 = curr[:i] + str((int(curr[i]) + 1 + 10) % 10) + curr[i + 1:]
                child2 = curr[:i] + str((int(curr[i]) - 1 + 10) % 10) + curr[i + 1:]
                if dis + 1 < minDis[int(child1)] and child1 not in deadSet:
                    minDis[int(child1)] = dis + 1
                    queue.append((child1, dis + 1))

                if dis + 1 < minDis[int(child2)] and child2 not in deadSet:
                    minDis[int(child2)] = dis + 1
                    queue.append((child2, dis + 1))

        if minDis[t] == sys.maxint:
            return -1
        return minDis[t]

