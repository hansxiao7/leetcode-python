import heapq


class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        m = len(maze)
        n = len(maze[0])

        visited = [[0 for j in range(n)] for i in range(m)]
        dis_m = [[sys.maxint for j in range(n)] for i in range(m)]
        dis_m[start[0]][start[1]] = 0

        # Dijkstra
        heap = [(0, start)]

        while len(heap) != 0:
            dis, node = heapq.heappop(heap)

            if visited[node[0]][node[1]] == 1:
                continue

            if node == destination:
                return dis

            visited[node[0]][node[1]] = 1

            for i in range(4):  # action
                pos, diss = next_pos(maze, node, i)
                if visited[pos[0]][pos[1]] == 0 and dis + diss < dis_m[pos[0]][pos[1]]:
                    dis_m[pos[0]][pos[1]] = dis + diss
                    heapq.heappush(heap, (dis + diss, pos))

        if visited[destination[0]][destination[1]] == 0:
            return -1
        else:
            return dis_m[destination[0]][destination[1]]


def next_pos(maze, curr, action):
    distance = 0
    m = len(maze)
    n = len(maze[0])
    result = [curr[0], curr[1]]
    if action == 0:  # up
        while result[0] > 0 and maze[result[0] - 1][result[1]] != 1:
            result[0] -= 1
            distance += 1

    elif action == 1:  # down
        while result[0] < m - 1 and maze[result[0] + 1][result[1]] != 1:
            result[0] += 1
            distance += 1

    elif action == 2:  # left
        while result[1] > 0 and maze[result[0]][result[1] - 1] != 1:
            result[1] -= 1
            distance += 1

    elif action == 3:  # right
        while result[1] < n - 1 and maze[result[0]][result[1] + 1] != 1:
            result[1] += 1
            distance += 1

    return result, distance