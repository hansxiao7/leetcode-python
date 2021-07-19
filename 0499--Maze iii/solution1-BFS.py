class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        m = len(maze)
        n = len(maze[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        dis = [[sys.maxint for i in range(n)] for j in range(m)]
        dis[ball[0]][ball[1]] = 0
        route = [['' for i in range(n)] for j in range(m)]

        # BFS
        queue = [ball]
        while len(queue) != 0:
            p = queue.pop(0)
            visited[p[0]][p[1]] = 1

            for i in ['u', 'd', 'l', 'r']:
                next_p, distance = next_pos(maze, p, i, hole)
                if distance + dis[p[0]][p[1]] < dis[next_p[0]][next_p[1]]:
                    dis[next_p[0]][next_p[1]] = distance + dis[p[0]][p[1]]
                    route[next_p[0]][next_p[1]] = route[p[0]][p[1]] + i
                    queue.append(next_p)
                elif distance + dis[p[0]][p[1]] == dis[next_p[0]][next_p[1]]:
                    if route[p[0]][p[1]] + i < route[next_p[0]][next_p[1]]:
                        route[next_p[0]][next_p[1]] = route[p[0]][p[1]] + i
                        queue.append(next_p)
        if visited[hole[0]][hole[1]] == 0:
            return 'impossible'
        return route[hole[0]][hole[1]]


def next_pos(maze, curr, action, hole):
    distance = 0
    m = len(maze)
    n = len(maze[0])
    result = [curr[0], curr[1]]
    if action == 'u':  # up
        while result[0] > 0 and maze[result[0] - 1][result[1]] != 1:
            result[0] -= 1
            distance += 1
            if result == hole:
                break

    elif action == 'd':  # down
        while result[0] < m - 1 and maze[result[0] + 1][result[1]] != 1:
            result[0] += 1
            distance += 1
            if result == hole:
                break

    elif action == 'l':  # left
        while result[1] > 0 and maze[result[0]][result[1] - 1] != 1:
            result[1] -= 1
            distance += 1
            if result == hole:
                break

    elif action == 'r':  # right
        while result[1] < n - 1 and maze[result[0]][result[1] + 1] != 1:
            result[1] += 1
            distance += 1
            if result == hole:
                break

    return result, distance