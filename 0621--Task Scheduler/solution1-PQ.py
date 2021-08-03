import heapq


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)

        # PQ
        dict1 = {}
        heap = []
        for task in tasks:
            dict1[task] = dict1.get(task, 0) + 1

        for key in dict1.keys():
            heapq.heappush(heap, (-dict1[key], key))

        result = 0
        while len(heap) != 0:
            count = 0
            temp = []
            for i in range(n + 1):
                if len(heap) != 0:
                    t_val, t = heapq.heappop(heap)
                    count += 1
                    if t_val + 1 < 0:
                        temp.append((t_val + 1, t))

            for i in range(len(temp)):
                heapq.heappush(heap, temp[i])

            if len(heap) != 0:
                result += n + 1
            else:
                result += count

        return result