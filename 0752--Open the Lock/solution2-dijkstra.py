import heapq


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        queue = [(0, '0000')]
        deadSet = set(tuple(deadends))
        if '0000' in deadSet:
            return -1

        visited = set()

        t = int(target)

        while len(queue) != 0:
            dis, curr = heapq.heappop(queue)

            if curr == target:
                return dis

            if curr in visited:
                continue

            visited.add(curr)

            for i in range(4):
                child1 = curr[:i] + str((int(curr[i]) + 1 + 10) % 10) + curr[i + 1:]
                child2 = curr[:i] + str((int(curr[i]) - 1 + 10) % 10) + curr[i + 1:]
                if child1 not in deadSet and child1 not in visited:
                    heapq.heappush(queue, (dis + 1, child1))

                if child2 not in deadSet and child2 not in visited:
                    heapq.heappush(queue, (dis + 1, child2))

        return -1

