import heapq


class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        # (dis, worker, bike)
        n_worker = len(workers)
        n_bike = len(bikes)

        heap = []

        for i in range(len(workers)):
            worker = workers[i]
            for j in range(len(bikes)):
                bike = bikes[j]
                dis = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                heapq.heappush(heap, (dis, i, j))

        result = [-1 for _ in range(n_worker)]
        bike_v = set()

        while len(heap) != 0:

            _, w, b = heapq.heappop(heap)

            if result[w] != -1 or b in bike_v:
                continue

            bike_v.add(b)
            result[w] = b

        return result


