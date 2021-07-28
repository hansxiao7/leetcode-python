class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # Bellman
        min_dis = [[sys.maxint for _ in range(n)] for _ in range(k + 2)]
        min_dis[0][src] = 0

        for n_line in range(1, k + 2):
            min_dis[n_line][src] = 0
            for edge in flights:
                x = edge[0]
                y = edge[1]
                cost = edge[2]

                min_dis[n_line][y] = min(min_dis[n_line][y], min_dis[n_line - 1][y], min_dis[n_line - 1][x] + cost)

        if min_dis[-1][dst] == sys.maxint:
            return -1
        return min_dis[-1][dst]