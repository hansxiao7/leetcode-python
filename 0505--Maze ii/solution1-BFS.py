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

        # BFS
        queue = [start]

        while len(queue) != 0:
            p = queue.pop(0)

            visited[p[0]][p[1]] = 1

            for i in range(4):
                next_p, dis = next_pos(maze, p, i)
                if dis_m[p[0]][p[1]] + dis < dis_m[next_p[0]][next_p[1]]:
                    dis_m[next_p[0]][next_p[1]] = dis + dis_m[p[0]][p[1]]
                    queue.append(next_p)

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