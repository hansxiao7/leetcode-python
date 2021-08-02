class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        k = len(costs[0])

        if n == 0:
            return 0

        if n == 1:
            return min(costs[0])

        min_color = -1
        second_min_color = -1

        for i in range(k):
            if min_color == -1 or costs[0][i] < costs[0][min_color]:
                second_min_color = min_color
                min_color = i
            elif second_min_color == -1 or costs[0][i] < costs[0][second_min_color]:
                second_min_color = i

        for i in range(1, n):
            new_min_color = -1
            new_second_min_color = -1

            for j in range(k):
                if j == min_color:
                    costs[i][j] += costs[i - 1][second_min_color]

                else:
                    costs[i][j] += costs[i - 1][min_color]

                if new_min_color == -1 or costs[i][j] < costs[i][new_min_color]:
                    new_second_min_color = new_min_color
                    new_min_color = j
                elif new_second_min_color == -1 or costs[i][j] < costs[i][new_second_min_color]:
                    new_second_min_color = j

            min_color = new_min_color
            second_min_color = new_second_min_color

        print(costs)
        print(second_min_color)

        return costs[n - 1][min_color]